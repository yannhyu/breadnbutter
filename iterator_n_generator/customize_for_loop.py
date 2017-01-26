# customize_for_loop.py

def countdown(n):
    print('Counting from', n)
    while n > 0:
        yield n    # Emit a value
        n -= 1
    print('Done')

if __name__ == '__main__':
    for x in countdown(6):    # Use countdown to feed for loop
        print(x)