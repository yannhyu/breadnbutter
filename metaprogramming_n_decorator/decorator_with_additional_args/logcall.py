# logcall.py

from functools import wraps

def logformat(fmt):
    def logged(func):
        # Idea: give me a function, I'll put
        # logging around it
        print('Adding logging to', func.__name__)

        @wraps(func)    # This copies func name and all the doc strings over
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        return wrapper
    return logged