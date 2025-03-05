# An Optional Else Block with a For Loop in Python
# The else block is executed if the loop terminates normally (the condition becomes false).
# The else block will not be executed if the loop is terminated by a break statement.
# The else block will not be executed if the loop is terminated by an exception.
# The else block will not be executed if the loop is terminated by a return statement.
# The else block will not be executed if the loop is terminated by a continue statement.
# The else block will not be executed if the loop is terminated by a goto statement.

# Example: Program to add natural numbers up to n
# sum = 1+2+3+...+n
# To take input from the user,
n = int(input("Enter n: "))
# initialize sum and counter
sum = 0
for i in range(1, n+1):
    sum = sum + i
else:
    print("The sum is", sum)
    
