# statistical significance & p-values
# p-values: what is the chance what we 
# observed was due to chance rather than
# due to real facts??

from statistics import mean, stdev
from random import shuffle

# birth weights from group given the drug
drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]

# birth weights from the other group given placebo
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]

# start with descriptive statistics 
# to see if there is any observed difference
print(mean(drug))
print(mean(placebo))
obs_diff = mean(drug) - mean(placebo)
print(f'difference between the drug mean and placebo mean is {obs_diff}')

# it raises the question: was that difference real
# or was it due to chance??

# One way to find out is called permutation test:
# assuming NULL hypothesis, (totally due to chance)
# we ought to be freely swapping the participants 
# between the two controlled groups and get the same
# results: as extreme as we observed here.

# Re-shuffling the data
# Taking the participants from the two groups and
# randomly re-label them, or re-assign them to the
# groups; or put it another way: when we permute it
# how often does it change the outcome?

# first combine the two groups
comb = drug + placebo

# number of drug group
nd = len(drug)

shuffle(comb)

# get the new drug group
print(comb[:nd])

# get the new placebo group
print(comb[nd:])

# If we shuffle (permuting or relabeling) the participants,
# is the new mean diff the same or more extreme than we
# observed?

def trial():
    shuffle(comb)
    drug = comb[:nd]
    placebo = comb[nd:]
    new_diff = mean(drug) - mean(placebo)
    # is the new mean diff the same or more extreme?
    return new_diff >= obs_diff

# our usual minimum repeat trial times
n = 10000

# how often do we get that result?
how_often_get_that_result = sum(trial() for i in range(n)) / n
print(f'P-value is {how_often_get_that_result}')
