
class Foo(object):
    foo = 'attr foo of Foo'


class Bar(object):
    foo = 'attr foo of Bar'
    bar = 'attr bar of Bar'


class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'


fb = FooBar()
print(fb.foo)




class A1():
#      def who_am_i(self):
#          print("I am a A1")
    pass

class A2():
     def who_am_i(self):
         print("I am a A2")

class A3():
     def who_am_i(self):
         print("I am a A3")

class B(A1, A2):
#     def who_am_i(self):
#         print("I am a B")
    pass

class C(A3):
    def who_am_i(self):
        print("I am a C")

class D(B,C):
#     def who_am_i(self):
#         print("I am a D")
    pass

d1 = D()
print(D.mro())
d1.who_am_i()

#
# class X():
#     def who_am_i(self):
#         print("I am a X")
#
#
# class Y():
#     def who_am_i(self):
#         print("I am a Y")
#
#
# class A(X, Y):
#     def who_am_i(self):
#         print("I am a A")
#
#
# class B(Y, X):
#     def who_am_i(self):
#         print("I am a B")
#
#
# class F(A, B):
#     def who_am_i(self):
#         print("I am a F")
#
#
#
# f = F()
# f.who_am_i()




