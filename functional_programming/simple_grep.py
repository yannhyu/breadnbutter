# simple_grep.py

def simplegrep(pattern, filename):
    with open(filename) as fin:
        for linenum, line in enumerate(fin):
            if pattern in line:
                print(linenum, ':', line)