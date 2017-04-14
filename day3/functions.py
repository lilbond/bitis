
def greet():
    print("Hi")


def greet_again(message):
    print(message)


def greet_again_with_type(message):
    print(type(message))
    print(message)


greet()
greet_again("Hello Again")
greet_again_with_type("One Last Time")
greet_again_with_type(1234)


# multiple types

def multiple_types(x):
    if x < 0:
        return -1
    else:
        return "Returning Hello"


print(multiple_types(-2))
print(multiple_types(10))


# variable arguments

def var_arguments(*args): # args will be tuples containing all the values
    for value in args:
        print(value)


var_arguments(1, 2, 3)


a = [1, 2, 3]
var_arguments(a)
var_arguments(*a) # expanding


def key_arg(**kwargs):
    for key,value in kwargs.items():
        print(key, value)

v
b = {"first" : "python", "second" : "python again"}

key_arg(b)