
# Loop in Python is a block of code that is executed repeatedly until a certain condition is met.
# Python has two types of loops: 
#   for loop 
#   while loop.

#INFO: For Loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.
# Syntax:
# for val in sequence:
#     Body of for

# Example:
# Program to find the sum of all numbers stored in a list
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in numbers:
    sum = sum + val
# Output: The sum is 48
print("The sum is", sum)


# INFO: while Loop
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# We generally use this loop when we don't know the number of times to iterate beforehand.
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



# INFO: The range() function
# We can generate a sequence of numbers using the range() function.
# range(10) will generate numbers from 0 to 9 (10 numbers).
# We can also define the start, stop, and step size as range(start, stop, step size).
# step size defaults to 1 if not provided.
# This function does not store all the values in memory; it would be inefficient. So it remembers the start, stop, step size, and generates the next number on the go.
# To force this function to output all the items, we can use the function list().
# The following example will clarify this.

# Example:
# Output: range(0, 10)
print(range(10))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10)))
# Output: [2, 3, 4, 5, 6, 7]
