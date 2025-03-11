'''
Lambda function
    - Anonymous function
    - Lambda function is a small anonymous function
    - It can take any number of arguments, but can only have one expression
    - The expression is evaluated and returned
    - Lambda functions can be used wherever function objects are required
    - Lambda functions are syntactically restricted to a single expression
    - Lambda functions are used to create small, one-time, anonymous function objects in Python

    syntax:
        lambda arguments: expression
            - arguments: The arguments to the function
            - expression: The expression to be evaluated and returned   


'''

# Example 1: Lambda function to add two numbers
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Example 2: Lambda function to square a number
def squareX(x):
    return x*x
print("using function:",squareX(6))  # Output: 36

square = lambda x: x*x
print("use lambda:",square(5))  # Output: 25