
# List
# List is a collection of items that are ordered and changeable. Allows duplicate members.
# List are written with square brackets"[]".
# List can contain any type of data.
# List can be nested.
# List are mutable.
# In List, We can access the elements by referring to the index number. Index starts from 0.
# List append the original list with the new element. It does not return a new list.

friend = ['Rolf', 'Anne', 'Charlie', 3, 25.65, False, ] # List with mixed elements
l1 = [3, 5, 1, 2, 4] # List with integer
empty = [] # Empty list


print(friend) # Output: ['Rolf', 'Anne', 'Charlie', 3, 25.65, False]
print(type(friend))  # Output: <class 'list'>
print(friend[0])  # Output: Rolf

# List element manipulation
friend[0] = 'John'
print(friend[0])  # Output: John