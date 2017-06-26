# list_concatenation.py

s = [10, 20, 30]
t = [40, 50, 60]

u = s + t
print(u)

# take first two
first_two = u[:2]

# take last two
last_two = u[-2:]

print(first_two + last_two)


s = 'abracadabra'
i = s.index('c')
print(i)
print(s[i])
print(s.count('c'))
print(s.count('a'))


s = [10, 5, 70, 2]
# in place sort
s.sort()
print(s)

s = [10, 5, 70, 2]
t = sorted(s)
print(t)
print(s)
