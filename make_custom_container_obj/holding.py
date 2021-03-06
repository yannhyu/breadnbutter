# holding.py

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):    # Making debug easy, used by the print function, meant for developers
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)        

    def __str__(self):    # for output, lower level, used by interpreter
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

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

#def read_portfolio(filename):
#    portfolio = []
#    with open(filename, 'r') as f:
#        rows = csv.reader(f)
#        headers = next(rows)
#        for row in rows:
#            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
#            portfolio.append(h)
#    return portfolio


if __name__ == '__main__':
    #portfolio = read_portfolio('../Data/portfolio.csv')
    portfolio = Portfolio.from_csv('../Data/portfolio.csv')    