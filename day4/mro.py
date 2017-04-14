# class A1(object):
#     pass
#
#
# class A2(object):
#     pass
#
#
# class A3(object):
#     pass
#
#
# class B(A1, A2):
#     pass
#
#
# class C(A1, A2, A3):
#     pass
#
#
# class D(B, C):
#     pass
#
#
# print(D.__mro__)


class A(object):
    pass


class B(A):
    pass


class C(object):
    pass


class D(A, C):
    pass


class E(B, D):
    pass


print(E.__mro__)


# E, B, D, C, A, O