# defaultdict_basic.py

from collections import defaultdict

s = 'mississippi'
kwargs = {'m':11,'s':12,'p':13}    #Give head start on some
d = defaultdict(int, **kwargs)

for k in s:
    d[k] += 1

print(d.items())    