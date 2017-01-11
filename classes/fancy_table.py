# fancy_table.py

from holding import read_portfolio
import table

portfolio = read_portfolio('../Data/portfolio.csv')

table.print_table(portfolio, ['name', 'shares'])    # allow cherry pick columns
print()
table.print_table(portfolio, ['name', 'shares', 'price'])    # allow cherry pick columns
print()
table.print_table(portfolio, ['shares', 'price', 'name'])    # allow cherry pick columns



