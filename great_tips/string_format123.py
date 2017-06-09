r1 = ['10', '1009769698', '20161128', 'Medlytix Insurance Found - Demographic Information Change']
r2 = ['10', '1009769698', '20161128', 'Medlytix Insurance Found']
r1.append('\n')
r2.append('\n')
results = [r1, r2]

for result in results:
    print("%-2s%-12s%-8s%-100s%s" % tuple(result))

for result in results:
    #print(tuple(result))
    print('{:2}{:12}{:8}{:100}{}'.format(*tuple(result)))





