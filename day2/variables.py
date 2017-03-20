
# This is a global variable
a = 0

if a == 0:
    # This is still a global variable
    b = 1


def my_function(c):
    # this is a local variable
    d = 3
    print(c)
    print(d)

# Now we call the function, passing the value 7 as the first and only parameter
my_function(7)

# a and b still exist
print(a)
print(b)

# c and d don't exist anymore -- these statements will give us name errors!
# print(c)
# print(d)


def add(a, b):       # This is a function definition. Note the colon (:)
    c = a+b          # This line belongs to the function because it's indented
    return c         # This line also belongs to the same function
print(add(1, 2))  # This line is OUTSIDE the function block


# scope of variables, by default assignment operator always creates variable in local scope

a = 0


def my_function():
    print(a)
my_function()


def my_function1():
    a = 3
    print(a)

my_function1()

print(a)


def my_function2():
    global a
    a = 3
    print(a)

my_function2()

print(a)


a = 0


def my_function3():
    # print(a)  this is an error. now a is local scope
    a = 3
    print(a)

my_function3()

# what is scope of each variable below


def my_function4(a):
    b = a - 2
    return b

c = 3

if c > 2:
    d = my_function4(5)
    print(d)


a = 5
b = 2
if a > b:
    print(a)
else:
    print(b)


l = [1, 'abc', 'c']
for element in l:
    print(element)


s = set(l)
for element in s:
    print(element)


my_map = {
    'one' : 1,
    'two' : 2,
    'three' : 3
}


for key in my_map.keys():
    print('key = {}  and value = {}'.format(key, my_map[key]))


for key, value in my_map.items():
    print(key, value)


# Let play with functions again :)
def greet_again():
    print("Hello Again")


# how about passing an argument
def greet_again(message):
    print(message)


# what is argument type?
def greet_again_type(message):
    print(type(message))
    print(message)


greet_again('Hello')
greet_again_type(123)
greet_again_type("Hello with type")


# no return type required, what does that mean?
def multiple_types(x):
    if x < 0:
        return "Return String!"
    else:
        return 0

print(multiple_types(1))
print(multiple_types(-1))


# how to pass variable arguments
# Arbitrary number of positional arguments
def var_arg_function(*args): # args will be a tuple containing all values that are passed in
    for i in args:
        print("printing", i)


var_arg_function(1, 2, 3)


# If you have an array, expand it using *
a = [1, 2, 3, 5]
var_arg_function(*a)


# Arbitrary number of keyword arguments
def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)


func(value1=1, value2=2, value3=3)
func()
my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)


for i in [0, 1, 2, 3, 4]:
    print(i)


# for loop with break
for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break


# note the range built in function
for i in range(5):
    print(i)


# for with continue
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)


# While with break
i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1


# Below we have a break, will the code end?
while True:
    for i in range(1,5):
        if i == 2:
            break    # Will only break out of the inner loop!
    print('1')


# nested loops with return in place of break
def break_loop():
    for i in range(1, 5):
        if i == 2:
            return(i)
        print(i)
    return(5)

break_loop()

for x in range(1, 6):
    print(x)


for x in range(1, 6):
    print(x)