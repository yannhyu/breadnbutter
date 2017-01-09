# read_port.py
# test git
from . import reader    # Package-relative import

def read_portfolio(filename, *, errors='warn'):
    '''
    Read a CSV file with name, date, shares, price data into a list
    '''
    return reader.read_csv(filename, [str, str, int, float], errors=errors)


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print(portfolio)

    total = 0.0
    for holding in portfolio:
        total += holding['shares'] * holding['price']

    print('Total cost:', total)
