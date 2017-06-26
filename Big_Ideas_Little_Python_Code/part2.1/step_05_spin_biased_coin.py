# step_05_spin_biased_coin.py
from random import * 
from statistics import *
from collections import *

# 5 or more heads from 7 spins of a biased coin
pop = ['heads', 'tails']
wgt = [6, 4]
# Cumulative weight
cumwgt = [0.60, 1.00]

# a spin
print(choices(['heads', 'tails'], cum_weights=[0.60, 1.00]))

# another spin
print(choices(['heads', 'tails'], cum_weights=[0.60, 1.00]))

# seven spins
seven_spins = choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7)
print(seven_spins)
print(seven_spins.count('heads'))