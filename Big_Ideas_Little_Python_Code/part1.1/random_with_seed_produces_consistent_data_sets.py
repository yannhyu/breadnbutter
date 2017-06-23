# random_with_seed_produces_consistent_data_sets.py

from random import *

print(random())
seed(8675309)
print(random())
print(random())
print(random())

seed(8675309)    # The same seed
print(random())
print(random())
print(random())
