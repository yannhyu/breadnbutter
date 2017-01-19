# logcall.py

from functools import wraps

def logged(func):
    # Idea: give me a function, I'll put
    # logging around it
    print('Adding logging to', func.__name__)

    @wraps(func)    # This copies func name and all the doc strings over
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper
