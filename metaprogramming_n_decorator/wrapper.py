# wrapper.py

def add(x, y):
    return x+y

def add_wrapper(*args, **kwargs):
    print('Wrapping !')
    return add(*args, **kwargs)


print(add_wrapper(2, 3))
print(add_wrapper(y=3, x=2))
print(add_wrapper(2, y=3))

"""
(dabeaz) yann.yu@mllxv-yu:metaprogramming_n_decorator$ python wrapper.py 
Wrapping !
5
Wrapping !
5
Wrapping !
5

"""