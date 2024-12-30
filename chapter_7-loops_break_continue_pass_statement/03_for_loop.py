
#For Loop
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



# for loop using range() function
# range function generates a sequence of numbers
# syntax:
#  range(start, stop, step_size)  # step_size defaults to 1 if not provided
#  range(10)  # generates numbers from 0 to 9 (10 numbers)


for i in range(5):
    print(i)

# Output: 1 2 3 4 5 6 7 8 9 10