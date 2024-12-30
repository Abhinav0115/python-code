# Set in Python

'''
# Set is a collection of unique elements. No duplicate elements are allowed in a set.
# Set is mutable, unordered and unindexed.
# Set is represented by curly braces {}.
# Set can also be created using set() constructor.
# Set can have elements of different data types.
# Set is iterable, i.e., we can iterate over the elements of a set.
# Set is dynamic, i.e., we can add or remove elements from a set.
# Set is not hashable, i.e., we cannot use set as a key in a dictionary.
# Set is not subscriptable, i.e., we cannot access elements of a set using index.
# Set is not sliceable, i.e., we cannot slice a set.
'''

#empty set
s = set()
print(type(s)) # <class 'set'>
dic= {} # This is a dictionary not a set
print(type(dic)) # <class 'dict'>


# Creating a set
s = {1, 2, 3, 4, 5}
print(s) # {1, 2, 3, 4, 5}


# Creating a set using set() constructor
s = set([11, 32, 35, 84, 56, "hero", 3.14])
print(s) # {1, 2, 3, 4, 5, 3.14, 'hero'}



# difference between discard() and remove() method is that if the element is not present in the set, remove() method raises KeyError whereas discard() method does not raise any error.

print("------------------------------------------------")
s.discard(32) # 32 is not present in the set
print(s) # {1, 2, 3, 4, 5, 3.14, 'hero'}

s.remove(32)  # 32 is not present in the set
print(s) # {1, 2, 3, 4, 5, 3.14, 'hero'}