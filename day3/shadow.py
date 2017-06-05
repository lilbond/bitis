
class C:
    x = 2  # class variable

    def __init__(self, y):
        self.y = y  # instance variable

print(C.x)
print(C.y) # AttributeError: type object 'C' has no attribute 'y'

c1 = C(3)
print(c1.x)
print(c1.y)

c2 = C(4)
print(c2.x) # 2
print(c2.y) # 4

#shadowing a class variable

c2.x = 4
print(c2.x) # 4
print(C.x) #2