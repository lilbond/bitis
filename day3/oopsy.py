
"""A class with an instance variable."""
class MyClass(object):
    def __init__(myself, value):
        #print(value)
        myself.instance_var = value
        myself.var2 = 2

    def print_me(myself):
        myself.var3 = 1234
        print(myself.instance_var)

    def add(self, x):
        print(x+2)

    def print_again(self):
        self.var4 = "i am var4"
        #print(self.xyz)
# create an object
obj = MyClass("It is an instance variable")

obj.print_again()

obj.xyz = 987
#print(obj.xyz)
obj.print_again()




obj1 = MyClass("any string")
obj1.print_again()

# obj1 = MyClass("I am another one")
# obj.print_me() # == MyClass.print_me(obj)
# obj1.print_me()
# obj1.print_again()
# obj.add(5)

# access an object data members
# print(obj.instance_var)
#
# print("\n\n-------- Class With Methods -----------")
#
#
# class MyClassWithMethod(object):
#     def __init__(self, value):
#         self.instance_var = value
#
#     def my_method(self):
#         return self.instance_var
#
# obj = MyClassWithMethod(1)
#
# # That is how we access method
# print(obj.my_method())
#
# print("\n\n-------- Class With Class Member -----------")
#
#
# # class with class members
# class MyClassWithMembers:
#     class_var = 2
#
# # Access class member with class name directly
# print(MyClassWithMembers.class_var)
#
# obj1 = MyClassWithMembers()
# obj2 = MyClassWithMembers()
#
# # Access class member with objects
# print(obj1.class_var)
# print(obj2.class_var)
#
# # Setting value for class member with class
# MyClassWithMembers.class_var = 3
#
# # value stayed same across
# print("value stayed same across")
# print(MyClassWithMembers.class_var)
# print(obj1.class_var)
# print(obj2.class_var)
#
#
# # Setting value for class member via object
# obj1.class_var = 4
#
# print(MyClassWithMembers.class_var)
#
# '''
# value for obj1 has changed, obj1 did not have class_var
# member and thus it got added as member for obj1.
# '''
# print(obj1.class_var)
# print(obj2.class_var)
#
#
# class Dog:
#     kind = 'canine'         # class variable shared by all instances
#
#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance
#
# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.kind)                  # shared by all dogs
# print(e.kind)                  # shared by all dogs
# print(d.name)                  # unique to d
# print(e.name)                  # unique to e
#
#
# e.kind = "abc"
# print(d.kind)
# print(e.kind)
# print(Dog.kind)