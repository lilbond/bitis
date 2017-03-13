
'''
A class with an instance variable.
'''
class MyClass(object):
    def __init__(self, value):
        self.instance_var = value

# create an objet
obj = MyClass("It is an instance variable")

print("\n\n-------- Class With Methods -----------")

# access an object data members
print(obj.instance_var)

class MyClassWithMethod(object):
    def __init__(self, value):
        self.instance_var = value

    def my_method(self):
        return self.instance_var

obj = MyClassWithMethod(1)

# That is how we access method
print(obj.my_method())

print("\n\n-------- Class With Class Member -----------")

# class with class members
class MyClassWithMembers:
    class_var = 2

# Access class member with class name directly
print(MyClassWithMembers.class_var)

obj1 = MyClassWithMembers()
obj2 = MyClassWithMembers()

# Access class member with objects
print(obj1.class_var)
print(obj2.class_var)

# Setting value for class member with class
MyClassWithMembers.class_var = 3

# value stayed same across
print(MyClassWithMembers.class_var)
print(obj1.class_var)
print(obj2.class_var)


# Setting value for class member via object
obj1.class_var = 4

print(MyClassWithMembers.class_var)

'''
value for obj1 has changed, obj1 did not have class_var
member and thus it got added as member for obj1.
'''
print(obj1.class_var)
print(obj2.class_var)
