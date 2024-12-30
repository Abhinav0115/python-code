# write a python program to detect double spaces in a string

a = "This is a string with double  spaces"

print(a.find("  "))

print(a) # original string is not changed because strings are immutable in python. String remains the same even by running the function on it.