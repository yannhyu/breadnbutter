# discrete_distribution.py

from random import choice, choices, sample, shuffle

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']

print('single choice:')
print(choice(outcomes))
print(choice(outcomes))
print(choice(outcomes))
print()

print('multiple choices:')
print(choices(outcomes, k=10))
print(choices(outcomes, k=10))
print()

from collections import Counter
print(Counter(choices(outcomes, k=10)))

# With large sample size, the distribution ought to be even
print(Counter(choices(outcomes, k=10000)))
print()

# Unless we introduce weighted distribution
print(Counter(choices(outcomes, [5, 4, 3, 2, 1], k=10000)))
print()