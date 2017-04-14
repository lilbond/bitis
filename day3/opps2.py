

class Person(object):
    """A simple class."""  # docstring
    species = "Homo Sapiens"  # class attribute

    def __init__(self, name):  # special method
        """This is the initializer. Constructor."""
        self.name = name  # instance attribute

    def __str__(self):  # special method
        """This function is run when Python tries to cast the object to a string.
        Return this string when using print(), etc.
        """
        return self.name

    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is " + self.name)

x = Person("Anuj")
y = Person("Rajesh")


print(x.name)
print(x.__str__())
print(y.name)


class A(object):
    def f(self, x):
        return 2 * x

a = A()
print(A.f(a,2))
print(a.f(2))


class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)

print(D.f)
print(D.f(12))
print(D.g)
print(D.g("world"))
