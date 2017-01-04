# read_port.py

import csv
import glob

def read_portfolio(filename, *, errors='warn'):
    '''
    Read a CSV file with name, date, shares, price data into a list
    '''
    if errors not in { 'warn', 'silent', 'raise', 'not interested' }:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise', \
                         'not interested'")

    portfolio = []    # List of records

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)    # Skip the header row
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise    # Reraise the last exception
                else:
                    pass
                continue
            record = tuple(row)
            portfolio.append(record)

        return portfolio


#files = glob.glob('Data/*.csv')
#print(files)

#for filename in files:
#    print(filename, read_portfolio(filename, errors='warn'))

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)

total = 0.0
for name, date, shares, price in portfolio:
    total += shares * price

print('Total cost:', total)
