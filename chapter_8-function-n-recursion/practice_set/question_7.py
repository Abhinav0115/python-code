'''
Q. Write a python program to convert inches to centimeter.

'''

def inch_to_cm(inch):
    return inch * 2.54


inch = float(input("Enter the length in inches: "))
print(f"{inch} inches is equal to {inch_to_cm(inch)} cm")

