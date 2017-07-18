# statistical significance & p-values
# p-values: what is the chance what we 
# observed was due to chance rather than
# due to real facts??

from statistics import mean, stdev

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