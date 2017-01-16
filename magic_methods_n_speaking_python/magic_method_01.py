# magic_method_01.py

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):    # magic method
        print('Add', other)


if __name__ == '__main__':
    p = Point(2, 3)
    p + 10
    p + [1, 2, 3]
    p + (4, 5)                 