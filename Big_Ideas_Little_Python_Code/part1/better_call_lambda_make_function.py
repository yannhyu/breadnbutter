# better_call_lambda_make_function.py

# Make a function that squares something
square_this = lambda x: x**2
print(square_this(5))
print((lambda x: x**2)(6))


# two arguments case
some_new_f = lambda x, y: 3*x + 4*y
print(some_new_f(3, 8))

# another useful case
# getting a computation ready, but delay
# running it until later
x = 10
y = 20

# no argument
run_this_f_later = lambda : x ** y

# As promised, now run it
res = run_this_f_later()
print(res)    # 100000000000000000000