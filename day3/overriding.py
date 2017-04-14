
class Base:
    def m1(self):
        print("in base m1")


class Sub(Base):
    def m2(self):
        print("in Sub m2")


s = Sub()
s.m1()
s.m2()

