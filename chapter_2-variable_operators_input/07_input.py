
# By default, the input() function returns a string.
a = input("Enter a number: ")
print("You entered: ", a) 
print(type(a))  # <class 'str'>

# take input as integer 
# we can convert the input to an integer by using the int() function. Similarly, we can convert the input to a float by using the float() function.
b = int(input("Enter a number: "))
print("You entered: ", b)
print(type(b))  # <class 'int'>

c = int(a)
print("You entered: ", c)
print(type(c))  # <class 'int'>


# Sum of two numbers
print("Sum of two numbers b + a: ", b + c)