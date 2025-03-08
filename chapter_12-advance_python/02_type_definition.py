'''
Type Definition in Python
    - Type hinting is a feature added in Python 3.5 which allows you to specify the type of variables.
    - Type hinting is a way to specify the type of a variable in Python.
    - Type hinting is optional and not enforced by Python.
    syntax:
        variable_name: type
        
        def function_name(variable_name: type) -> return_type:
            pass

'''


# Example 1: Type Definition

a: int = 5
b: str = "Hello, World!"
c: float = 5.5

def add(a: int, b: int) -> int:
    return a + b

print(add(a, 10))  # Output: 15