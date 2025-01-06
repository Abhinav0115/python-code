'''
Q. Write a python program using function to convert celsius to fahrenheit.

'''


def f_to_c():
    '''Program to convert celsius to fahrenheit'''
    c = float(input("Enter temperature in celsius:"))
    return ((c/5)*9) + 32

f = f_to_c()
print(f"Temperature in Farhenheit is {round(f,2)}")


