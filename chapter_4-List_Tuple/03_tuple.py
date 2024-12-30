# Tuple is a collection of immutable Python objects.
# Tuple is a collection of items that are ordered and unchangeable. Allows duplicate members.
# Tuple are written with round brackets "()".
# Tuple can contain any type of data.
# Tuple can be nested.
# In Tuple, We can access the elements by referring to the index number. Index starts from 0.
# Tuple does not support item assignment.
# Tuple is faster than List.
'''
# Uses of Tuple
    Tuple is used for read-only data.
    Tuple is used for dictionary keys.
    Tuple is used in string formatting.
    Tuple is used in function arguments.
    Tuple is used in return statement.
    Tuple is used in multiple assignment.
'''

tpl = ('Rolf', 'Anne', 'Charlie', 3, 25.65, False, ) # Tuple with mixed elements
a = (1, 2, 3, 4, 5) # Tuple with integer elements
empty  = () # Empty tuple 

# if we want to create a tuple with single element, we need to add a comma after the element.
# if we does not add a comma, it will be considered as a string or integer.
one_element = ("herro",) # Tuple with single element
print(type(one_element))  # Output: <class 'tuple'>


print(tpl)  # Output: ('Rolf', 'Anne', 'Charlie', 3, 25.65, False)
print(type(tpl))  # Output: <class 'tuple'>
print(tpl[0])  # Output: Rolf

# Tuple element manipulation
# tpl[0] = 'John'  # TypeError: 'tuple' object does not support item assignment
