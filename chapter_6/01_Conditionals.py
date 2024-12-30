
# Conditonal statements are used to execute code based on a condition. 


# The most common conditional statement is the if statement.
# Other conditional statements include the elif and else statements.

# The if statement is used to execute a block of code if a condition is true.
# The elif statement is used to execute a block of code if the previous condition is false and the current condition is true.
# The else statement is used to execute a block of code if all the previous conditions are false.

# The syntax of the if statement is as follows:
# if condition:
#     block of code

# The syntax of the elif statement is as follows:
# if condition:
#     block of code
# elif condition:
#     block of code
# else:
#     block of code

# The block of code is indented to indicate that it is part of the if statement.
# The condition is a boolean expression that evaluates to either True or False.

# The block of code is executed only if the condition is true. If the condition is false, the block of code is not executed and the program moves on to the next statement. If all statements are false, the else block is executed.


age = int(input("Enter your age: "))

# if else statement
if age < 18 and age > 0:
    print("You are a minor")
else :
    print("You are an adult")  