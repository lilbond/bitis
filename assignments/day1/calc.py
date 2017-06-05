def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


def client():
    print("Sum of 10, 2 is : " + str(add(10, 2)))
    print("Difference of 10, 2 is : " + str(subtract(10, 2)))
    print("Multiplication of 10, 2 is : " + str(mul(10, 2)))
    print("Division of 10, 2 is : " + str(divide(10, 2)))


client()