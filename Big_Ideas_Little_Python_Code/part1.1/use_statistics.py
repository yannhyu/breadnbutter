# use_statistics.py

from statistics import mean, median, mode, stdev, pstdev

# Descriptive statistics
print(mean([50, 52, 53]))
print(median([50, 52, 53]))
print(median([51, 50, 52, 53]))
# most popular
print(mode([51, 50, 52, 53, 51, 51]))
# Divide by (n-1)
print(stdev([51, 50, 52, 53, 51, 51]))
# Divide by n
print(pstdev([51, 50, 52, 53, 51, 51]))

