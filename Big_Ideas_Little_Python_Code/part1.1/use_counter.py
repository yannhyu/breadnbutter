# use_counter.py

from collections import Counter

d = {}
try:
    print(d['dragon'])
except KeyError as ker:
    print(f'KeyError on dragon: {ker}')

# Counter is modelled after 'bag' in smalltalk
d = Counter()
print(d['dragon'])

d['dragon'] += 1
print(d['dragon'])
print(d)

color_counter = Counter('red green red blue red blue green purple'.split())
print(color_counter)

print(color_counter.most_common(1))
print(color_counter.most_common(2))

# be able to list all elements is useful for analytics
print(list(color_counter.elements()))

print(list(color_counter))
print(list(color_counter.values()))
print(list(color_counter.items()))