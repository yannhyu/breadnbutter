
from read_port_into_list_of_dicts import read_portfolio

portfolio = read_portfolio('Data/portfolio.csv')

names = [holding['name'] for holding in portfolio]
unique_names = set(names)
print(unique_names)

# or use set comprehension
print({holding['name'] for holding in portfolio})
