#NOTE:
# Function is a group of statements that perform a specific task.
# Function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# A function can be reused in a program many times.

# Syntax:
# def function_name(parameters):
#     """docstring"""
#     statement(s)

# def is a keyword that defines a function.
# function_name is the name of the function.
# parameters are the values passed to the function.
# docstring is a description of the function.
# statement(s) is a block of code that performs a specific task.


# ------------- Function Call -------------
# Once a function is defined, you can call it by using the function name followed by parentheses.
# You can pass data, known as arguments, into a function.
# You can call a function as many times as needed.

# Syntax:
# function_name(arguments)

# function_name is the name of the function.
# arguments are the values passed to the function.


# ------------- Function Without Parameters -------------
# A function can be defined without parameters.
    # def function_name():
    #     """docstring"""
    #     statement(s)

# A function can be called without arguments.
    # function_name()


# ------------- Example: -------------
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")
    print(f"Hello, {name}. Good morning!")

# calling function
greet('Paul') # Output: Hello, Paul. Good morning!
greet('Ram') # Output: Ram, Paul. Good morning!