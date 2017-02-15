# step_1_pipeline.py

import os
import time
import csv

def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue    # Retry
        yield line

def grep(names, rows):
    for row in rows:
        if row[0] in names:
            yield row

def converted(rows):
    types = [str, float, str, str, float, float, float, float, int]
    return ( [func(val) for func, val in zip(types, row)] for row in rows )

def downchanged(converted_matchings):
    return ( row for row in converted_matchings if row[4] < 0 )                   

if __name__ == '__main__':
    lines = follow('../Data/stocklog.dat')
    rows = csv.reader(lines)
    matchings = grep({'MSFT', 'IBM', 'CAT', 'AA'}, rows)
    converted_matchings = converted(matchings)
    downstocks = downchanged(converted_matchings)
    for row in downstocks:
            name = row[0]
            price = row[1]
            change = row[4]
            print('{:>10s} {:>10.2f} {:>10.2f}'.format(name, price, change))

