"""
Samples below are intended to get us started with Python.
Did you notice this is a multi-line comment :-) and yes being the first
one and before code, it qualifies to be documentation as well. How Cool!!!

In order to be a docstring it had to be multi-line
"""

# print hello world :-), Hey this is a single line comment
print("Hello, World")

'''
We can define strings using ' (single quotes) or using " (double quotes)
Same goes for comments, did you notice this one.

Assignment
----------

print messages below:

1. You won't be disappointed with Python
2. One day you will say "I love Python"
3. You won't be disappointed with Python. One day you will say "I love Python"
'''

# Getting rid of new line
print("Hello", end='')
print(", World!!!")

# Working with variables is damn easy
an_int = 1
a_string = "We won't work with other types today. Yes, there are many more."

'''
There is no verbosity like - int anInt = 1; or String aString = "Something";
'''

# Programming is all about decision making, is not it?
if an_int == 1:
    print(a_string)

# A decision without a negative case is not so useful
if an_int == 2:
    print(a_string)
else:
    print("Damn it was not true!!!")

# Ah! that was nice but how can I take more than one decisions
if an_int == 2:
    print("It is 2 indeed")
elif an_int == 1:
    print("It is 1 indeed")
else:
    print("I seriously have not idea, what it is")

'''
Do we just keep scripting in Python or can we package snippets and reuse
Did not you realize, what print is? Yes, it is a function.

A callable, reusable and self contained unit of code. Provides a logical grouping and
helps in organizing snippets to perform unit of work.

Disclaimer: I am NOT good at definitions and this one is purely self cooked :-)
'''


def greet_awesome_people():
    print("Hello Awesome People. I am a dumb function but teaches a very powerful thing. \nGuess what?")


# Guess what?
greet_awesome_people()


# Same goes for me, guess guess :-)
def i_am_bit_smarter(message):
    print(message)


# And same goes for me
def i_am_bit_more_smarter(a, b):
    return a + b


i_am_bit_smarter("Custom Message>> Sum of 10 and 2 is : " + str(i_am_bit_more_smarter(10, 2)))

'''
Assignment
----------

Write the smartest calculator which:
- Works only with integer
- Handles add, subtract, mul and divide

client should be able to use your calculator like:
add(10,2), subtract(11, 3) etc.
'''


# Time to evaluate your guess and may be bit of programming Moksha :-).