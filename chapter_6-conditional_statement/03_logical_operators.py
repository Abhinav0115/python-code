# There are three logical operators in Python: and, or, and not.

# The "and" operator returns True if both the operands are True. Otherwise, it returns False.
# The "or" operator returns True if at least one of the operands is True. Otherwise, it returns False.
# The "not" operator returns True if the operand is False. Return False if the operand is True.

# The following code snippet demonstrates the use of logical operators in Python:

# Logical operators
a = 5
b = 10
c = 15

# and operator
if a < b and b < c:
    print("Both conditions are true")

# or operator
if a < b or b > c:
    print("At least one condition is true")

# not operator
if not a > b:
    print("The condition is false")

    