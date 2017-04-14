def foo(x):
    x[0] = 9
    x = [1, 2, 3]
    x[2] = 8
    print(x)

y = [4, 5, 6]
foo(y)
print(y)
