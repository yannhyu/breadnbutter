# adv_func_args_unpacking.py

def f(*args):
    a, b, *rest_of_args = args
    print(a)
    print(b)
    print(rest_of_args)


if __name__ == '__main__':
    f(1, 2, 3)
    f('x', 'y', 'z', 'a', 'b', 'c')
    other_args = tuple(range(10))
    f(*other_args)