# sample.py

from logcall import logformat

@logformat('You called ... {func.__name__}')
def add(x, y):
    '''
    Want this doc string to show when wrapped
    '''
    return x + y

@logformat('Calling ... {func.__name__}')
def sub(x, y):
    return x - y

def mul(x, y):
    return x * y
