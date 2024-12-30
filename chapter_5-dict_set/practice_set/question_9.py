'''
Q. Can you change the values inside a list which is contained in set s?

s = {8, 7, 12, "Harry", [1, 2]}
'''



s = {8, 7, 12, "Harry", [1, 2]}

print(s) # TypeError: unhashable type: 'list'

# We can't use list in set because list is mutable and mutable objects are unhashable.
# So, we can't use list in set. 

# No, we can't change the values inside a list which is contained in set s.
# Because, set s is unhashable type: 'list'.
