# customize_iteration.py

def grep(pattern, filename):
    with open(filename) as fh:
        for line in fh:
            if pattern in line:
                yield line


if __name__ == '__main__':
    for line in grep('IBM', '../Data/portfolio.csv'):
        print(line)
