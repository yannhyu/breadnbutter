# step_05_spin_biased_coin.py
from random import * 
from statistics import *
from collections import *

# Use lambda expression to represent a deferred computation
# seven spins, do we get 5 or more heads?
trial = lambda: choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >= 5

# computation is executed when we call it
print(trial())
print(trial())

# now we conduct large number of trials
n = 100000
# res = [trial() for i in range(n)]
# print(res)
# print(sum(res) / n)
print(sum(trial() for i in range(n)) / n) 
