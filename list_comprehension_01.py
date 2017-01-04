
from read_port_into_list_of_dicts import read_portfolio

portfolio = read_portfolio('Data/portfolio.csv')

print(portfolio)

total = sum([holding['shares']*holding['price'] for holding in portfolio])
print(total)

# Collecting data
names = [holding['name']  for holding in portfolio]
print(names)

# Filtering data
morethan100shares = [holding for holding in portfolio if holding['shares'] > 100]
print(morethan100shares)
