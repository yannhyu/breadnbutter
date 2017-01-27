# grep_via_generator_expression.py
filename = '../Data/portfolio.csv'
pattern = 'IBM'
with open(filename) as fh:
    catches = (line for line in fh if pattern in line)
    for line in catches:
        print(line)
