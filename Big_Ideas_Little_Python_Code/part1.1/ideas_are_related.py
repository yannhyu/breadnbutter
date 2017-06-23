# ideas_are_related.py

from random import choice, choices, sample, shuffle

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']

# choice is a special case of sample
print(sample(outcomes, k=1)[0])
print(choice(outcomes))
print()

# shuffle is a special case of sample
shuffle(outcomes); print(outcomes)
print(sample(outcomes, k=len(outcomes)))

