# regular_generator_is_meant4one_time_use.py

def countdown(n):
    print('Counting from', n)
    while n > 0:
        yield n    # Emit a value
        n -= 1
    print('Done')

if __name__ == '__main__':
    cd = countdown(6)
    for x in cd:    # Use countdown to feed for loop
        print(x)

    print('2nd round ...', cd)
    for x in cd:    # No longer available for repeated use
        print(x)       