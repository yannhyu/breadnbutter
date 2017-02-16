# step_6_extended_use_of_yield.py

# normal use of yield to emit something
def gen():
    n = 5
    while n > 0:
        yield n
        n -= 1

# extended use of yield
def coro():
    n = 0
    while True:
        result = yield n    # Emitting and receiving a result
        print('Got:', result)
        n += 1

if __name__ == '__main__':
    g = gen()
    for x in g:
        print(x)

    print('.....')
    c = coro()
    print(c)
    print(c.__next__())    # Wake up the generator
    print(c.send('HEY'))
    print(c.send('Apple'))

