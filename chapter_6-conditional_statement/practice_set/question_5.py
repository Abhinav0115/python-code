'''
Q. Write a program to find out the given name is present in the list or not.

'''

name = ["abhi", "gaurav", "shek", "anand", "ram", "rina"]

entered_name = input("Enter name: ")

if entered_name in name:
    print("your name is present in the list")
else:
    print("your name is not present in the list")