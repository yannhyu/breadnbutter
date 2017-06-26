# step_09_median_of_5_fall_in_the_middle_of_2_quartiles.py

# Motivation is to improve the implementation of statistics
# median
# How good of a pivot point does 5 samples picking the
# median give us?

# Do we need a larger number?
# A good median falls in the 2nd or 3rd quartile;
# the middle 2/3 of the population??
# How often does a median of 5 fall in those areas?
from random import *
from statistics import *

# sample pop of size 5
sample_pop_of_size_5 = sample(range(100000), 5)
print(sample_pop_of_size_5)
print(sorted(sample_pop_of_size_5))
print(median(sample_pop_of_size_5))

# the 2nd of sorted pop ought to be the median
print('median is:')
print(sorted(sample_pop_of_size_5)[2])
print()

# If population size is 100k
# we want to know if median falls
# between 25k and 75k?
n = 100000
second_quartile = n // 4
third_quartile = n * 3 // 4
print(f'For a population of {n}')
print(f'We want median to fall inside {second_quartile} and {third_quartile}')