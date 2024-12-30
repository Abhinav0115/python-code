
a = int(input("Enter your age: "))


# if elif else statement
if( a < 18 and a > 0):
    print("You are a minor")
elif( a >= 18 and a < 60):
    print("You are an adult")
elif( a >= 60):
    print("You are a senior citizen")
else:
    print("Invalid age")

print("End of program")