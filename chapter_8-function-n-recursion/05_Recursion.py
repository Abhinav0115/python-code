
#NOTE: Recursion
# Recusion is a technique where a function calls itself to solve a problem.
# Recursion is used to solve problems that contain smaller subproblems.
# The base case is the condition that stops the recursion. Without a base case, the function will call itself indefinitely.
# The recursive case is the condition that allows the function to call itself with a modified input.
# Recursion is a powerful technique that can be used to solve complex problems.

# Example: Factorial
# The factorial of a number n is the product of all positive integers less than or equal to n.
# The factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# The factorial of 5 is 5 * factorial(4).
# The factorial of 4 is 4 * factorial(3).

# IMP: The factorial of 0 and 1 is 1.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n =  int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")

