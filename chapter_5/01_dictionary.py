
'''
# Dictionary is a collection of key-value pairs where each key is unique and immutable.
# Dictionary is mutable, unordered and indexed.
# Dictionary is created using curly braces {}.
# Dictionary is also known as associative array or hash map.
# Dictionary keys are case-sensitive. 
# Dictionary values can be of any data type.
# Dictionary keys must be immutable data types like string, number or tuple.
# Dictionary values can be mutable or immutable data types.
'''

# Creating an empty dictionary
e = {} 

# Creating a dictionary
a = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_married": True,
    "total_marks": 95.25,
    0: "Zero",
}

print(a) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'is_married': True, 'total_marks': 95.25}

print(type(a)) # Output: <class 'dict'>

print(a.get("name")) # Output: John

print(a["age"]) # Output: 30


'''
# difference between get() and [] notation in dictionary access is that get() method returns None if the key does not exist, while [] notation raises KeyError. 
# get() method is useful when you are not sure if the key exists in the dictionary or not.
# get() method can also return a default value if the key does not exist.
# get() method does not raise an error if the key does not exist.
'''
print(a.get("is_student")) # Output: None
print(a.get("is_student", "hell o")) # Output: hell o  -> we assign a default value to the key

'''
# a[<key>] method is useful when you are sure that the key exists in the dictionary.
# a[<key>] method raises an error if the key does not exist.
# a[<key>] method does not return a default value if the key does not exist.
'''
# print(a["is_student"]) # Output: KeyError: 'is_student'