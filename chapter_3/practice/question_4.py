# write a python program to replace the double spaces in a string with single spaces.

a = "This is a string with double  spaces"

# print(a.find("  "))


print(a.replace("  ", " "))

print(a) # original string is not changed because strings are immutable in python. String remains the same even by running the function on it.