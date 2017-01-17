# holding_validated_refactored_02.py

class Typed(object):
    expected_type = object

    def __init__(self, name):
        self.name = name    

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
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


class Holding(object):
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
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
    portfolio = Portfolio.from_csv('../Data/portfolio.csv')    