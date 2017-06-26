# shuffle_n_sample_wo_dup.py
from random import choices, shuffle, sample

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']

shuffle(outcomes)
print(outcomes)
print()

# With choices, there may be dup
print('Sampling with replacement:')
print(choices(outcomes, k=5))
print()

# Use sample to avoid dups
print('Sampling without replacement:')
print(sample(outcomes, k=4))
print(sample(outcomes, k=4))
print()