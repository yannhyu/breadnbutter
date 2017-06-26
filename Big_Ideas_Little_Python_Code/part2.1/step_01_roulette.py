# step_01_roulette.py

from random import *
from statistics import *
from collections import *

# Six roulette wheels -- 18 red 18 black 2 greens
# print(['red'] * 18)
a_roulette = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
print(a_roulette)
print(choice(a_roulette))

# Six rounds
print([choice(a_roulette) for i in range(6)])

# Let's see how we did for six rounds
print(Counter([choice(a_roulette) for i in range(6)]))

# Another way for playing six rounds
print(choices(a_roulette, k=6))
print(Counter(choices(a_roulette, k=6)))