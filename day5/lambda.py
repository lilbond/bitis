def greeting():
    return "Hello"

print(greeting())


greet = lambda : "Hello"

print(greet())

# take arguments

strip_and_upper_case = lambda s: s.strip().upper()

strip_and_upper_case("  Hello   ")


# take arbitrary number of arguments / keyword arguments

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')


l = [1, -2, 3, -4, 5, 7]
l = list(filter(lambda x: x>0, l))
print(l)

my_list = [1, -2, 3, -4, 5, 7]
print(my_list)
l = list(map(lambda x: abs(x), my_list))
print(l)
