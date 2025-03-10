'''
Raising Exception:
    - We can raise an exception explicitly using the raise keyword.
    - We can raise an exception of a specific type.
    - We can also provide a message with the exception.
    - We can raise an exception in the try block and handle it in the except block.
    
'''



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
else:
    print("Division is: ", a/b)