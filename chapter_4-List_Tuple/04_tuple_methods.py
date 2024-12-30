# Tuple methods

tpl = ('Rolf', 'Anne', 'Charlie', 3, 25.65, False, 'Charlie',) # Tuple with mixed elements
t1 = (3, 5, 1, 2, 4) # Tuple with integer elements



# 1. Tuple count - Count the number of times an element appears in the tuple
count = tpl.count('Charlie')
print(count)  # Output: 2



# 2. Tuple index - Get the index of the element (it will return the first occurrence of the element)
idx = tpl.index('Charlie')
print(idx)  # Output: 2
# print(tpl.index('C'))  # Output: ValueError: tuple.index(x): x not in tuple



# 3. Tuple len - Get the length of the tuple
length = len(tpl)
print(length) # Output: 7



# 4. Tuple slicing - Get the specific range of elements from the tuple
sliced = tpl[1:4]
print(sliced) # Output: ('Anne', 'Charlie', 3)



# 5. Tuple concatenation - Concatenate two tuples
tpl2 = ('Smith', 'Bob')
tpl3 = tpl + tpl2
print(tpl3) # Output: ('Rolf', 'Anne', 'Charlie', 3, 25.65, False, 'Charlie', 'Smith', 'Bob')



# 6. Tuple repetition - Repeat the tuple elements
tpl4 = tpl * 2
print(tpl4) # Output: ('Rolf', 'Anne', 'Charlie', 3, 25.65, False, 'Charlie', 'Rolf', 'Anne', 'Charlie', 3, 25.65, False, 'Charlie')



# 7. Tuple membership - Check if the element is present in the tuple
is_present = 'Charlie' in tpl
print(is_present) # Output: True



# 8. Tuple min - Get the minimum element from the tuple
min_value = min(t1)
print(min_value) # Output: 1



# 9. Tuple max - Get the maximum element from the tuple
max_value = max(t1)
print(max_value) # Output: 5



# 10. Tuple sum - Get the sum of all elements from the tuple
sum_value = sum(t1)
print(sum_value) # Output: 15



# 11. unpacking tuple - Unpack the tuple elements into variables 
a, b,c , *rest = t1
print(a, b, c, rest) # Output: 3 5 1 [2, 4]