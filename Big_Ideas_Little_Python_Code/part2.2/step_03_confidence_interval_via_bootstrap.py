# step_02_timings_of_network_events.py
from statistics import mean, stdev
from random import choices

timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98,
           8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]

print(f'original sample: {timings}')
print(f'mean: {mean(timings)}')
print(f'standard deviation: {stdev(timings)}')

# Build a 90% confidence interval
def bootstrap(data):
    # make another sample with replacement
    # from the same sample
    return choices(data, k=len(data))


if __name__ == '__main__':
    re_sample_01 = bootstrap(timings)
    print(f're-sample with replacement: {re_sample_01}')    

    # get the mean
    print(f'mean: {mean(re_sample_01)}')

    # if we do enough number of re-sampling 
    # we can get the confidence interval

    # at least do this many 
    n = 10000
    # get that many means
    means = sorted(mean(bootstrap(timings)) for i in range(n))
    print(len(means))
    print(means[:20])
    print(means[-20:])
    print(mean(means))

    # for 90% confidence interval, that is 5% on each side
    print(round(n * 0.05))    # 500 on each side
    print(means[500])
    print(means[-500])
    print(f'The observed mean of {mean(timings)}')
    print(f'Falls in a 90% confidence interval from {means[500] :.1f} to {means[-500] :.1f}')   
