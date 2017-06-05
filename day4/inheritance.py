
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super().__init__(s, s)

s = Square(4)
print(s.area())


print(Square.mro())

#
# def area1(self):
#     return self.w + self.w
#
# s.area = area1
#
# print(s.area(s))

