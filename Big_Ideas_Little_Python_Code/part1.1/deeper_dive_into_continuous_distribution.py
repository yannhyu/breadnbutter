# deeper_dive_into_continuous_distribution.py

from random import *
from statistics import mean, stdev

print('... 1000 using triangular:')
# Make 1k randoms with triangular
data = [triangular(1000, 1100) for i in range(1000)]
print(f'mean : {mean(data)}')
print(f'stdev: {stdev(data)}')
print()

print('... 1000 using uniform:')
# Make 1k randoms with uniform
data = [uniform(1000, 1100) for i in range(1000)]
print(f'mean : {mean(data)}')
print(f'stdev: {stdev(data)}')
print()

print('... 1000 using gaussian:')
# Make 1k randoms with uniform
data = [gauss(100, 15) for i in range(1000)]
print(f'mean : {mean(data)}')
print(f'stdev: {stdev(data)}')
print()

print('... 1000 using expovariate:')
# Make 1k randoms with expovariate
data = [expovariate(20) for i in range(1000)]
print(f'mean : {mean(data)}')
print(f'stdev: {stdev(data)}')
print()