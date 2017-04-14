
class Base:
    def m1(self):
        print("in base m1")


class Sub(Base):
    def m2(self):
        print("in Sub m2")


s = Sub()
s.m1()
s.m2()


class Foo:
    foo = "foo"

class Bar:
    foo = "foo_from_bar"
    bar = "bar"


class FooBar(Foo, Bar):
    foobar = "foobar"

fb = FooBar
print(fb.foo)


class FooBar(Bar, Foo):
    foobar1 = "foobar1"

fb1 = FooBar
print(fb1.foo)

