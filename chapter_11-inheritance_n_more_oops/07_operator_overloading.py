'''
Operator Overloading:
    - Operators in Python can be overloaded using dunder methods.
    - These methods are called when a given operator is used on the objects.
    - These methods are defined using the __<dunder>__ syntax.
    - For example, to overload the + operator, we use the __add__(self, other) method.
    - The __add__(self, other) method is called when the + operator is used on the objects.

'''

'''
Different Dunder Methods:
    - __init__(self): It is used to initialize the object.
    - __del__(self): It is used to delete the object.
    - __add__(self, other): It is used to overload the + operator.
    - __sub__(self, other): It is used to overload the - operator.
    - __mul__(self, other): It is used to overload the * operator.
    - __truediv__(self, other): It is used to overload the / operator.
    - __floordiv__(self, other): It is used to overload the // operator.
    - __mod__(self, other): It is used to overload the % operator.
    - __pow__(self, other): It is used to overload the ** operator.
    - __and__(self, other): It is used to overload the & operator.
    - __or__(self, other): It is used to overload the | operator.
    - __str__(self): It is used to overload the str() function.
    - __len__(self): It is used to overload the len() function.
'''


'''
Example 1: Give us error as we are trying to add two objects of the class number.
    - To fix this, we need to overload the + operator using the __add__(self, other) method.
    - The __add__(self, other) method is called when the + operator is used on the objects.
    - The __add__(self, other) method takes two parameters, self and other. 


class number:
    a = 3
    b = 7

    def __init__(self, n):
        self.n = n

n = number(5)
m = number(2)

print(n + m) # TypeError: unsupported operand type(s) for +: 'number' and 'number'

'''


class number:
    a = 3
    b = 7

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

n = number(5)
m = number(2)

print(n + m) # 7