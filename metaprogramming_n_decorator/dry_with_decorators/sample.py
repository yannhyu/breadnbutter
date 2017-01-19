# sample.py

from logcall import logged

@logged
def add(x, y):
    '''
    Want this doc string to show when wrapped
    '''
    return x + y

@logged
def sub(x, y):
    return x - y

def mul(x, y):
    return x * y
