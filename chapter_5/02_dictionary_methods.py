# Dictionary Methods

a = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_married": True,
    "total_marks": 95.25,
    0: "Zero",
}


# 1. len() method - returns the number of items in the dictionary (key-value pairs)
print("len", len(a))



# items() method - returns a view object that displays a list of a dictionary's key-value tuple pairs
print(a.items())



# keys() method - returns a view object that displays a list of a dictionary's keys
print(a.keys())



# values() method - returns a view object that displays a list of a dictionary's values
print(a.values())



#update() method - updates the dictionary with the specified key-value pairs
a.update({"name":"doe"})
print(a)

a.update({"age": 25, "country": "USA"}) # If the key does not exist, it will be added
print(a)


# get(<key>) method - returns the value of the specified key
print(a.get("is_married"))

print(a.get("is_student")) # returns None as the key does not exist



# get(<key>, <default_value>) method - returns the value of the specified key, if the key does not exist, it returns the default value
print(a.get("is_student", False))



# copy() method - returns a copy of the dictionary
b = a.copy()
print(b)



# pop(<key>) method - removes the item with the specified key name
a.pop("is_married")
print(a)



# popitem() method - removes the last inserted item
a.popitem()
print(a)



# clear() method - removes all the elements from the dictionary
a.clear()