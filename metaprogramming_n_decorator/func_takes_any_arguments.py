# func_takes_any_arguments.py

def func(*args, **kwargs):
    print(args)
    print(kwargs)


func()
func(1, 2, 3, 4)
func(1, 2, x=4, y=3)

"""
(dabeaz) yann.yu@mllxv-yu:metaprogramming_n_decorator$ python func_takes_any_arguments.py 
()
{}
(1, 2, 3, 4)
{}
(1, 2)
{'y': 3, 'x': 4}

"""    