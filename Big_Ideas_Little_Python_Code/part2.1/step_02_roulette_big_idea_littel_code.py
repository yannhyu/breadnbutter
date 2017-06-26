# step_02_roulette_big_idea_littel_code.py
from random import *
from statistics import *
from collections import *

print(Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6)))