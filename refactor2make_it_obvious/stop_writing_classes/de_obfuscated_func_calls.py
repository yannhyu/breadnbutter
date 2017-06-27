# de_obfuscated_func_calls.py

def greet(greeting, target):
    return f'{greeting}! {target}'

import functools
greet_with_common_phrase = functools.partial(greet, 'Always saying the same shit to everyone')
print(greet_with_common_phrase('bob'))  