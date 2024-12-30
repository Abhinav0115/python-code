
### string function 

# In python, we have many built-in functions to perform operations on string. 
# Here are some of the functions which are used frequently.



# len() function is used to get the length of string.
# Syntax: len(string)
# It returns the length of string.

a = "Hello, World!"
print(len(a)) # Output: 13



# lower() function is used to convert the string to lower case.
# Syntax: string.lower()
# It returns the lower case version of string.

print(a.lower()) # Output: hello, world!



# upper() function is used to convert the string to upper case.
# Syntax: string.upper()
# It returns the upper case version of string.

print(a.upper()) # Output: HELLO, WORLD!



# capitalize() function is used to convert the first character of string to upper case and rest of the characters to lower case.
# Syntax: string.capitalize()
# It returns the capitalized version of string.

b = "hello, world!"
print(b.capitalize()) # Output: Hello, world!



# title() function is used to convert the first character of each word to upper case and rest of the characters to lower case.
# Syntax: string.title()
# It returns the title case version of string.

c = "hello, world!"
print(c.title()) # Output: Hello, World!



# strip() function is used to remove the leading and trailing white spaces from string.
# Syntax: string.strip()

b = "   Hello, World!   "
print(b.strip()) # Output: Hello, World!



# replace() function is used to replace a string with another string.
# Syntax: string.replace(old_string, new_string)
# It returns the string with replaced value.
# It will replace all the occurrences of old_string with new_string.

c = "Hello World Hello"
print(c.replace("Hello", "Hi")) # Output: Hi World Hi



# split() function is used to split the string into list of strings.
# Syntax: string.split(separator)
# It returns the list of strings.
# By default, separator is space.

d = "Hello World!"
print(d.split()) # Output: ['Hello', 'World!']

# We can also provide separator in split function.
e = "Hello,World!"
print(e.split(",")) # Output: ['Hello', 'World!']



# join() function is used to join the list of strings into single string.
# Syntax: separator.join(list)
# It returns the single string.
# separator is used to join the strings.

f = ["Hello", "World!"]
print(" ".join(f)) # Output: Hello World!



# find() function is used to find the index of substring in string.
# Syntax: string.find(substring)
# It returns the index of substring in string. If substring is not found, it returns -1.

g = "Hello, World!"
print(g.find("World")) # Output: 7
print(g.find("Python")) # Output: -1


# startswith() function is used to check if the string starts with given substring.
# Syntax: string.startswith(substring)
# It returns True if string starts with given substring else False.

h = "Hello, World!"
print(h.startswith("Hello")) # Output: True
print(h.startswith("World")) # Output: False


# endswith() function is used to check if the string ends with given substring.
# Syntax: string.endswith(substring)
# It returns True if string ends with given substring else False.

i = "Hello, World!"
print(i.endswith("World!")) # Output: True
print(i.endswith("Hello")) # Output: False