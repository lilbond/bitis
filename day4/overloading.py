

def func1(arg1, arg2=None):
    if arg2 is not None:
        print(arg1, arg2)
    else:
        print(arg1)


func1(1, 2)


def func2(arg1, *args):
    if args:
        for item in args:
            print(item)
    else:
        print(arg1)


func2(1, 2, 3, 4, 5)


def func3(arg1, **args):
    if args:
        for k, v in args.items():
            print(k, v)
    else:
        print(arg1)


func3(1, arg2=2, arg3=3)
func3(1)
func3(3, arg2=2, arg3=3)


#       |-positional-|-optional-|---keyword-only--|-optional-|
def func(arg1, arg2=10 , *args, kwarg1, kwarg2=2, **kwargs):
     pass