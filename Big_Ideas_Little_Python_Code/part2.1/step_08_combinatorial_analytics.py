# step_08_combinatorial_analytics.py

from math import factorial as fact
from random import * 

def comb(n, r):
    return fact(n) // fact(r) // fact(n-r) 

# What is the probability of getting heads?
ph = 0.6

# 5 heads out of 7 spins
print('7 spins the probability of getting 5 heads,')
getting_5_heads_out_of_7_spins = ph ** 5 * (1 - ph) ** 2 * comb(7, 5)
print(getting_5_heads_out_of_7_spins)
print()

# 6 heads out of 7 spins
print('7 spins the probability of getting 6 heads,')
getting_6_heads_out_of_7_spins = ph ** 6 * (1 - ph) ** 1 * comb(7, 6)
print(getting_6_heads_out_of_7_spins)
print()

# 7 heads out of 7 spins
print('7 spins the probability of getting 7 heads,')
getting_7_heads_out_of_7_spins = ph ** 7 * (1 - ph) ** 0 * comb(7, 7)
print(getting_7_heads_out_of_7_spins)
print()

# Our theoretocal result:
print('Our theoretical result:')
theoretical_res = (getting_5_heads_out_of_7_spins 
                   + getting_6_heads_out_of_7_spins
                   + getting_7_heads_out_of_7_spins)

print(theoretical_res)
print()

# Out empirical result
# seven spins, do we get 5 or more heads?
print('Our empirical result:')
trial = lambda: choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >= 5
n = 100000
print(sum(trial() for i in range(n)) / n)
print()