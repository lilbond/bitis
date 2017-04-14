
def append(elem, to=[]):
    to.append(elem)
    return to

print(append(1))
# Out: [1]

# Appends it to the internally stored list
print(append(2))
# Out: [1, 2]

# Using a new created list gives the expected result
print(append(3, []))
# Out: [3]

# will append to the internally stored list again
print(append(4))
# Out: [1, 2, 4]


def append(elem, to=None):
    if to is None:
        to = []

    to.append(elem)
    return to


def foo(x):
    x[0] = 9
    x = [1, 2, 3]
    x[2] = 8


y = [4, 5, 6]
foo(y)
print(y)











