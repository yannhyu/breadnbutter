# make_obj_callable.py

class Add(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print('Sum of {} and {} is:'.format(num1, num2))

    def __call__(self):
        return self.num1 + self.num2


add = Add(2, 3)
print(add())

from collections import defaultdict
s = 'mississippi'
kwargs = {'m':11,'s':12,'p':13}
d = defaultdict(add, **kwargs)
for k in s:
    d[k] += 1

print(d.items())       
