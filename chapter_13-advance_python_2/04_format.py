'''
.format() in Python
    - The format() method formats the specified value(s) and insert them inside the string's placeholder.
    - The placeholder is defined using curly brackets: {}
    - The format() method returns the formatted string.
    - The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.


'''

res = "{} is a good {} developer".format("David", "java")
print(res)

print("{} is a good {} developer".format("Rohan", "python"))

print("{1} is a good {0} developer".format("php", "Shyam"))
