
from read_port_into_list_of_dicts import read_portfolio

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)

print('... use lambda to sort by stock name .. :')
portfolio.sort(key=lambda holding: holding['name'])
for holding in portfolio:
    print(holding)

import itertools
for name, items in itertools.groupby(portfolio, key=lambda holding:
                                     holding['name']):
    print('NAME:', name)
    for it in items:
        print('     ', it)


