# four_types_of_continuous_distribution.py

from random import *

print('uniform:')
print(uniform(1000, 1100))
print()

print('triangular:')
print(triangular(1000, 1100))
print(triangular(1000, 1100))
print(triangular(1000, 1100))
print()

print('gaussian:')
# Average IQ and 15 stdev
# Generate random IQs
print(gauss(100, 15))
print(gauss(100, 15))
print(gauss(100, 15))
print()

# Used to simulate arrival time in a queue system
print('expovariate:')
print(expovariate(20))
print(expovariate(20))
print(expovariate(20))
print()