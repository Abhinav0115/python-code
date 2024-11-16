### String Slicing

# We can access a part of string using slicing.
# For slicing, we need to provide start index and end index.
# For left to right slicing, start index is 0 and right most index is n-1 where n is the length of string.  
# String can be also sliced in reverse order by providing negative index. Reverse Slicing right most index is -1. 
# Syntax: string[start_index:end_index]

# Example of String Slicing

a = "hello, world!"

sl = a[0: 4] # Slicing from 0 to 4
print(sl) # Output: hell

rsl = a[-6: -1] # Reverse Slicing from -6 to -1
print(rsl) # Output: world

# we can also print single character of string using slicing.
print(a[0]) # Output: h

# If we don't provide start index, it will start from 0.
print(a[:5]) # Output: hello

# If we don't provide end index, it will go till end of string.
print(a[7:]) # Output: world!

# If we don't provide both start and end index, it will return whole string.
print(a[:]) # Output: hello, world!

### Slicing with step

# In the above example, we have sliced the string using start and end index. We can also provide step in slicing.
# Step is used to skip the characters while slicing. 
# If step is 1, it will return all characters between start and end index. 
# If step is 2, it will return every 2nd character between start and end index. so on.
# Syntax: string[start_index:end_index:step]

x = "hello, world!"

sl = x[0: 10: 2] # Slicing from 0 to 10 with step 2
print(sl) # Output: hlo o