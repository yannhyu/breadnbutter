# new_f_str_formatter.py

x = 10

print('The answer is %d today' % x)
print('The answer is {0} today'.format(x))
print('The answer is {a} today'.format(a=x))

# available for python3.6+
print(f'The answer is {x} today')
print(f'The answer is {x :08d} today')
