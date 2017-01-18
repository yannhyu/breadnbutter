# func_that_makes_func.py

def add(x, y):
    def do_add():
        print('Adding {} + {} -> {}'.format(x, y, x+y))
        return x+y
    return do_add

a = add(2, 3)    # Delayed evaluation
print(a)
print(a())

b = add('hello', 'world')
print(b)
print(b())

"""
(dabeaz) yann.yu@mllxv-yu:func_as_obj$ python func_that_makes_func.py 
<function add.<locals>.do_add at 0x7f762edbb950>
Adding 2 + 3 -> 5
5
<function add.<locals>.do_add at 0x7f762edbba60>
Adding hello + world -> helloworld
helloworld

"""