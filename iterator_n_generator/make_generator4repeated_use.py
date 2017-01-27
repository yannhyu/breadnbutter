# make_generator4repeated_use.py

class Countdown(object):
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

if __name__ == '__main__':
    c = Countdown(5)
    for x in c:
        print(x)

    for y in c:    # Use the generator repeatedly
        print(y)