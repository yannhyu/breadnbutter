# example_of_func_as_input.py

names = ['dave', 'Thomas', 'Lewis', 'paula']    # mixed cases
print(names)

names.sort(key=lambda name: name.upper())
print(names)

ten_times = lambda x: 10 * x
print(ten_times(3))