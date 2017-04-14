

def print_msg(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)

    printer()

print_msg("Hello")


def print_msg(msg):

    def printer():
        print(msg)

    return printer

another = print_msg("Hello")
another()


del print_msg
another()


print_msg("Now")


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))