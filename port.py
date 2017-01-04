# port.py

import csv
import glob

def portfolio_cost(filename, *, errors='warn'):
    '''
    Computes total share*price for a csv file with name, date, shares, price
    data
    '''
    total = 0.0

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
                continue

            total += row[2] * row[3]

        return total


files = glob.glob('Data/*.csv')
print(files)

for filename in files:
    print(filename, portfolio_cost(filename, errors='not interested'))

