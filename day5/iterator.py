

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)

s = 'abc'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)

print('***** fib *****')
class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

for i in Fib(10):
    print(i)


print('**** print 0 to n-1 ****')
class CustomRange:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb

for i in CustomRange(10):
    print(i)


print('***** Fibonacci without Generator *****')
def fib(max):
    numbers = []
    a, b = 0, 1
    while a < max:
        numbers.append(a)
        a, b = b, a + b
    return numbers

print(fib(10))


print('***** Fibonacci using Generator *****')
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

gen = fib(10)
print(gen)
print(next(gen))


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

a = reverse('golf')
for char in a:
    print(char)
    break


'''a = reverse('golf')'''
print(a.__next__())


print('***** Fibonacci with infinite loop *****')
def fib():
    a, b = 0, 1
    while True:
        print(a)
        a, b = b, a + b

fib()
gen = fib(10)
print(gen)
print(next(gen))

