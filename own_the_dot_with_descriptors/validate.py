# validate.py

# Example of a descriptor
class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected int...')
        instance.__dict__[self.name] = value


class Point(object):
    x = Integer('x')    # Need to be applied at class level
    y = Integer('y')    # Act as supervisor or guardian
    def __init__(self, x, y):
        self.x = x
        self.y = y
