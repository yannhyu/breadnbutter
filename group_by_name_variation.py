
from read_port_into_list_of_dicts import read_portfolio

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)

print('... use lambda to sort by stock name .. :')
portfolio.sort(key=lambda holding: holding['name'])
for holding in portfolio:
    print(holding)

import itertools
by_name = { name: list(items) for name, items in itertools.groupby(portfolio, key=lambda holding:
                                     holding['name']) }
print(by_name['IBM'])
print(by_name['CAT'])
print(by_name)
