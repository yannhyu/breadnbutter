# simple_follow_stocks.py
"""
(dabeaz) yann.yu@mllxv-yu:breadnbutter$ pwd
/home/yann.yu/workspace/pythoncode/breadnbutter
(dabeaz) yann.yu@mllxv-yu:breadnbutter$ python stocksim.py
python: can't open file 'stocksim.py': [Errno 2] No such file or directory
(dabeaz) yann.yu@mllxv-yu:breadnbutter$ cd Data/
(dabeaz) yann.yu@mllxv-yu:Data$ python stocksim.py
"VZ",42.78,"6/11/2007","09:30.00",-0.29,42.95,42.78,42.78,119300
"CAT",77.99,"6/11/2007","09:30.00",-0.53,78.32,77.99,77.99,169282


yann.yu@mllxv-yu:processing_pipeline_workflow$ python simple_follow_stocks.py 
     "CAT"      78.14      -0.38
      "AA"      39.40      -0.26
     "MRK"      49.93      -0.21
      "PG"      62.72      -0.35
       "T"      39.97      -0.29
     "DIS"      34.14      -0.06
     "MCD"      50.99      -0.42
       "C"      53.04      -0.29
     "WMT"      49.82      -0.26
      "DD"      50.68      -0.45

"""
import os
import time

def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue    # Retry
        yield line

if __name__ == '__main__':
    for line in follow('../Data/stocklog.dat'):
        row = line.split(',')
        change = float(row[4])
        if change < 0:
            name = row[0]
            price = row[1]
            print('{:>10s} {:>10s} {:>10.2f}'.format(name, price, change))        