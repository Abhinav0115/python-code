'''
Dictionary merge operators:
    - The merge operators are used to merge dictionaries.
    - The merge operators are | and |=
    - The merge operators are used to merge two dictionaries.
    - The merge operators are used to merge dictionaries without modifying the original dictionaries.

    
    | operator:
        - The | operator is used to merge two dictionaries.
        - The | operator returns a new dictionary.
        - The | operator does not modify the original dictionaries.

    |= operator:
        - The |= operator is used to merge two dictionaries.
        - The |= operator modifies the original dictionary.
        - The |= operator returns None.
'''

dict1 = {'name': 'John', 'age': 25}
dict2 = {'city': 'New York', 'country': 'USA'}

# Using | operator
merged_dict = dict1 | dict2
print(merged_dict)    # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Using |= operator
dict1 |= dict2
print(dict1)    # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}