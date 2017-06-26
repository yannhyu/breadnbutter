# step_10_three_steps.py

# Question: what is the probability that the median
# of five samples falls in a middle quartile?
# Big idea: this is expressible in one short amd simpe line
# of Python
from random import *
from statistics import *

# define a large size
n = 100000

# build trials, via sampling without replacement
trial = lambda: n // 4 < median(sample(range(n), 5)) <= 3 * n // 4

# run trials
print(sum(trial() for i in range(n)) / n)
