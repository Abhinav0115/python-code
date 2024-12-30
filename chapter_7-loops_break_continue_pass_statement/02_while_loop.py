# while Loop
'''
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# if the loop is entered, the process of checking the condition and executing the block of code is repeated until the condition becomes false.
# We generally use this loop when we don't know the number of times to iterate beforehand.
'''
# Syntax:
# while test_expression:
#     Body of while

# Example:
# Program to add natural numbers up to n
# sum = 1+2+3+...+n
# To take input from the user,
n = int(input("Enter n: "))
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
# Output: The sum is 55
print("The sum is", sum)
