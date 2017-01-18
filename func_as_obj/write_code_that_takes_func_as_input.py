# write_code_that_takes_func_as_input.py

import time
def after(seconds, func):
    time.sleep(seconds)
    func()

def hello():
    print('Hello a little after...')

for i in range(1, 5):
    print('.')
    #time.sleep(1)

after(5, hello)

def greeting(name):
    print('hello to you', name)

for i in range(1, 5):
    print('.')
    time.sleep(1)
    
# after(5, greeting) won't work since it needs param
after(5, lambda: greeting('Yann'))
