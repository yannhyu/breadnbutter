# validate_advanced_experiment.py

class Typed(object):
    expected_type = object

    def __init__(self, name=None):    # Make name arg optional, so that 'name' can be altered after class creation
        self.name = name    

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):    # Intercepting the set method
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}...'.format(self.expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int
    def __set__(self, instance, value):
        super().__set__(instance, value)
        if value <= 0:
            raise ValueError('Must be > 0...') 


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str    


def typed(cls):
    cls._attributes = set()
    for key, value in vars(cls).items():
        if isinstance(value, Typed):
            value.name = key    # Fill in details: "name = String('name')"
            cls._attributes.add(key)
    return cls


class structuretype(type):
    def __new__(meta, name, bases, methods):
        cls = super().__new__(meta, name, bases, methods)
        cls = typed(cls)    # Apply a class decorator
        return cls

    def __init__(cls, name, bases, methods):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(methods)
        super().__init__(name, bases, methods)        


class Structure(metaclass=structuretype):
    def __setattr__(self, name, value):
        #if name not in { 'name', 'date', 'shares', 'price' }:
        print(name, '::', value)
        if name not in self._attributes:
            raise AttributeError('No attribute {}'.format(name))
        super().__setattr__(name, value)

    def __init__(self, name):
        super().__init__()
        self.name = self.__getattr__(name)

class Holding(Structure):    # Commonly used technique in frameworks (SQLAlchemy, Django)
    name = String()          # Base class supervises and manages class definition 
    shares = Integer()
    price = Float()
    date = String()
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):    # Making debug easy, used by the print function, meant for developers
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)        

    def __str__(self):    # for output, lower level, used by interpreter
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

import csv

class Portfolio(object):
    def __init__(self):
        self.holdings = []

    def __repr__(self):
        return '::'.join([ repr(h) for h in self.holdings ])

    def __len__(self):    # Helping our obj to be more like a list (1)
        return len(self.holdings)

    def __getitem__(self, n):    # Helping our obj to be more like a list (2) indexing
        if isinstance(n, str):    # Overload []: to customize it to fit the problem domain
            return [ h for h in self.holdings if h.name == n ]
        else:
            return self.holdings[n]

    def __iter__(self):    # Helping our obj to be more like a list (3) for loop
        return self.holdings.__iter__()

    def total_cost(self):
        return sum([ h.shares * h.price for h in self.holdings ])

    def current_value(self):
        pass

    def __getattr__(self, name):
        return getattr(self.holdings, name)    # Forward to internal list method

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                self.holdings.append(h)
        return self             


if __name__ == '__main__':
    portfolio = Portfolio.from_csv('../../Data/portfolio.csv')    