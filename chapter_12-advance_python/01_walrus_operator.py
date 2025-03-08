
'''
Walrus Operator in Python 
    - The walrus operator is a new operator introduced in Python 3.8. It is represented by :=.
    - The walrus operator is used to assign values to variables as part of an expression.


'''

# Example 1: Walrus Operator
if (n := len([1,2,3,4,5] )) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    


