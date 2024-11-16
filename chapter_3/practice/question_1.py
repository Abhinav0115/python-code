# write a pyhon program to display  good afternoon followed by user entered name using input() function

name = input("Enter your name: ")


print("Good Afternoon,", name )

# f-string: It is a way to format strings in Python. It is used to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.
print( f"Good Afternoon, {name}")  

result = "Good Afternoon, " + name
print(result)