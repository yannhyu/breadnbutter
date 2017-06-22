# use_counter.py

from collections import Counter

d = {}
try:
    print(d['dragon'])
except KeyError as ker:
    print(f'KeyError on dragon: {ker}')

d = Counter()
print(d['dragon'])

d['dragon'] += 1
print(d['dragon'])
print(d)

color_counter = Counter('red green red blue red blue green purple'.split())
print(color_counter)



