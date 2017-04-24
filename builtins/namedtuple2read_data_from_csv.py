# namedtuple2read_data_from_csv.py

from collections import namedtuple

CarRecord = namedtuple('CarRecord', 'id, name, price')

import csv

reader = csv.reader(open("sqlcars.csv", "r"))
next(reader, None)    #Skip the header row
for car in map(CarRecord._make, reader):
    print(car.id, car.name, car.price)