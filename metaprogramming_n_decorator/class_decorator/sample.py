# sample.py

from logcall import logged, logmethods

@logged
def add(x, y):
    '''
    Want this doc string to show when wrapped
    '''
    return x + y

@logged
def sub(x, y):
    return x - y

@logged
def mul(x, y):
    return x * y


@logmethods
class Spam(object):
    def __init__(self, value):
        self.value = value

    def yow(self):
        print('Yow !')    

    def grok(self):
        print('Grok !!')