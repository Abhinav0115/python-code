'''
Exception handling:
    - Exception handling is a mechanism to handle runtime errors.
    - It is a way to handle the exceptions that occur during the execution of the program.
    - except block is used to handle the exceptions.
    - We can use multiple except blocks to handle different exceptions.

    - we can also use else and finally block with the try-except block.
    - else block will execute if no exception occurs. i.e if try block executes successfully.
    - Finally block will execute always whether exception occurs or not. i.e it will always execute.
    - Finally block will execute even after the return statement.
    
    # syntax with try and except block:
    syntax:
        try:
            # code block where exception can occur
        except ExceptionName:
            # code block to handle the exception
    
    # syntax with else  block:       
    -  code inside else block will execute if no exception occurs. i.e if try block executes successfully.
    syntax:
        try:
            # code block where exception can occur
        except ExceptionName:
            # code block to handle the exception
        else:
            # code block to execute if no exception

    # syntax with else and finally block:       
    syntax:
        try:
            # code block where exception can occur
        except ExceptionName:
            # code block to handle the exception
        else:
            # code block to execute if no exception
        finally:
            # code block to execute always

'''
'''
Types of error in python:
    - Syntax Error
    - Logical Error
    - Runtime Error

Types of exceptions:
    - ZeroDivisionError
    - NameError
    - TypeError
    - ValueError
    - FileNotFoundError
    - ImportError
    - KeyboardInterrupt
    - IndexError
    - KeyError
    - indentationError

'''



# Example 1: ZeroDivisionError
try:
    a = 10/0
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("No exception occurred")
finally:
    print("This block will always execute")


print("------------------------------")

# Example 2:
try:
    a = int(input("Enter a number: "))
    print("Entered number is: ", a)

except Exception as e:
    print("Exception occurred: ", e)
else:
    print("No exception occurred")
 


print("------------------------------")

# Example 3: 
try:
    a = int(input("\nEnter a number:"))
    print("Entered number is: ", a)

except TypeError:
    print("Type error occurred")
except ValueError:
    print("Value error occurred")
except Exception as e:
    print("Exception occurred: ", e)