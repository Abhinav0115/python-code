# NOTE: 
# There are two types of functions in Python:
# 1. Built-in functions
# 2. User-defined functions


# NOTE: 
# 1. Built-in functions
# Python has many built-in functions that you can use directly. 
# For example, print(), input(), len(), etc. are built-in functions.

# NOTE:
# 2. User-defined functions
# You can define your functions in Python.
# You can define functions to provide the required functionality.
# Here are simple rules to define a function in Python:
# - Function blocks begin with the keyword def followed by the function name and parentheses ().
# - Any input parameters or arguments should be placed within these parentheses.
# - You can also define parameters inside these parentheses.
# - The first statement of a function can be an optional statement - the documentation string of the function or docstring.
# - The code block within every function starts with a colon (:) and is indented.
# - The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.


# ------------- Example: of user defined function -------------
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")
    
# calling function
greet('Paul') # Output: Hello, Paul. Good morning! 

# NOTE:
# ------------- Some of the most popular built-in functions are: -------------
# len()	    Returns the length of an object
# type()	Returns the type of an object
# print()	Prints the specified message to the screen
# input()	Allows user input
# int()	    Returns an integer number
# float()	Returns a floating-point number
# str()	    Returns a string
# list()	Returns a list
# tuple()	Returns a tuple
# dict()	Returns a dictionary
# set()	    Returns a set
# abs()	    Returns the absolute value of a number
# all()	    Returns True if all items in an iterable are true
# any()	    Returns True if any item in an iterable is true
# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	    Converts a number into a binary number
# bool()	Returns the boolean value of the specified object