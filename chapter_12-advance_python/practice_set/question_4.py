'''
write a program to display a/b, where a and b is an integer. If b=0 display infinite by handling the zerodivision error.

'''

try:
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))

    result = a/b
    print(result)
except ZeroDivisionError as z:
    print("infinite")