
import abc


class ABCClass(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')


class MyAbstractClass(ABCClass):
    pass

    # def __str__(self):
    #     return 'here i am!'


a = MyAbstractClass()
print(a)


