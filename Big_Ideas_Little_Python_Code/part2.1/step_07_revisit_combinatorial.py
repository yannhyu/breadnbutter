# step_07_revisit_combinatorial.py

# Compare to the analytic approach
from math import factorial as fact

print(fact(4))
print(fact(5))

def comb_decimal(n, r):
    return fact(n) / fact(r) / fact(n-r)


# take 3 out of ten things
print('this contains decimal:') 
print(comb_decimal(10, 3))
print()

# Do not like decimal so use floor division

def comb(n, r):
    return fact(n) // fact(r) // fact(n-r) 

# taking 2 at a time out of ten things 
print('no more decimal:')
print(comb(10, 2))
print()

# Now apply the binomial theorem
# What is the probability of getting heads?
ph = 0.6

# 5 heads out of 7 spins, for combinatorials 
# of 7 things taking 5 at a time
print('7 things taking 5 at a time,')
print('the probability of 5 heads of 7 spins:')
getting_5_heads_out_of_7_spins = ph ** 5 * (1 - ph) ** 2 * comb(7, 5)
print(getting_5_heads_out_of_7_spins)
print()
