'''
Q. How do you prevent a python print() function to print a new line at the end?

'''

# Solution: 
    # To prevent a python print() function to print a new line at the end, we can use end="" as an argument in the print() function.

print("a",)
print("b", end="")
print("c", )
print("d", )