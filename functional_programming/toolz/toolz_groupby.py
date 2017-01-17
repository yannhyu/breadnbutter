# toolz_groupby.py

from toolz import groupby

names = ['Terry', 'Alan', 'John', 'Christophe', 'Noel', 'Andy', 'Margie']
print(groupby(len, names))