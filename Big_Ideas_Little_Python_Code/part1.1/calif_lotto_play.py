# calif_lotto_play.py
from random import sample

# Calif lotto has 56 numbers, and we need to
# choose six, sampling with no replacement;
# the numbers are sorted
# when winning numbers are published,
print(sorted(sample(range(1, 57), k=6)))