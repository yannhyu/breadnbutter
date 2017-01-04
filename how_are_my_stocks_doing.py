
from read_port_into_list_of_dicts import read_portfolio

portfolio = read_portfolio('Data/portfolio.csv')

# list comprehension
names = [holding['name'] for holding in portfolio]
unique_names = set(names)
print(unique_names)

# or use set comprehension
print({holding['name'] for holding in portfolio})

# find out the current market prices of my stocks and
# find out whether it went up or down
namestr = ','.join(unique_names)
print(namestr)

import urllib.request
u = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(namestr))
data = u.read()
pricedata = data.split()
print(pricedata)

# Pairing up unique_names with pricedata
# turning pair of streams into stream of pairs
market_prices = dict(zip(unique_names, pricedata))
print(market_prices)

# dict comprehension
current_prices = { name: float(price) for name, price in zip(unique_names, pricedata) }
print(current_prices)

# find out the current value of portfolio
current_value = 0.0
current_value = sum([ holding['shares'] * current_prices[holding['name']] for
                     holding in portfolio ])

# get the original cost base
total_cost = sum([ holding['shares'] * holding['price'] for holding in
                  portfolio ])
print(current_value)
print(total_cost)
print(current_value - total_cost)
