# fancy_table_2.py

import table
from holding import read_portfolio

portfolio = read_portfolio('../Data/portfolio.csv')
formatter = table.TextTableFormatter(width=10)
table.print_table(portfolio, ['shares', 'price', 'name'], formatter)

formatter2 = table.TextTableFormatter(width=25)
table.print_table(portfolio, ['name', 'shares'], formatter2)

formatter3 = table.QuotedTextTableFormatter(width=33)
table.print_table(portfolio, ['name', 'shares'], formatter3)