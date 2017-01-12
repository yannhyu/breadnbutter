# fancy_table_use_multiple_inheritance.py

import table
from holding import read_portfolio

class Formatter(table.QuotedMixin, table.CSVTableFormatter):    # Compose behavior
    pass


class TextFormatter(table.QuotedMixin, table.TextTableFormatter):    # like logo
    pass    

portfolio = read_portfolio('../Data/portfolio.csv')
table.print_table(portfolio, ['name', 'shares'], Formatter())

table.print_table(portfolio, ['name', 'price', 'shares'], TextFormatter(width=33))

