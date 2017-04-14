

def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
        print("end")

f = foo()
g = f
print(next(f))
print(next(g))
print(next(f))

print(next(f))
# print(next(f))
#print(next(f))   #uncomment it and see
