# Set Methods

s = {11, 32, 54, 87, "hero", "zero", 74.12}
print(s)


# 1. len() method - Returns the number of elements in the set
print("len", len(s))



# 2. add() method - Adds an element to the set
s.add(100)
print(s)

s.add(54)  # 54 is already present in the set
print("add", s)



# 3. difference() method - Returns a set containing the difference between two or more sets
s1 = {11, 32, 54, 87, "hero", "zero", 74.12}
s2 = {11, 32, 54, 87, "hero", "zero", 74.12, 100, 22}

print("difference ",s2.difference(s1)) # This will return the value only element exist in s2 but not in s1. if no difference then it will return empty set

print("difference ",s1.difference(s2)) # This will return the value only element exist in s1 but not in s2. if no difference then it will return empty set



# 4. difference_update() method - Removes the items in the first set that are also included in another , specified set (s1 - s2)

s1 = {11, 32, 54, 87, "hero", "zero", 74.12, 55}
s2 = {11, 32, 54, 87, "hero", "zero", 74.12, 100, 22}

s1.difference_update(s2) # This will remove the element from s1 which is also present in s2
print("difference_update s1", s1)

s1 = {11, 32, 54, 87, "hero", "zero", 74.12, 55}
s2.difference_update(s1) # This will remove the element from s2 which is also present in s1
print("difference_update s2", s2)


# 5. remove() method - Removes an element from the set
s.remove(32)
print("remove",s)

# 32 is not present in the set
# s.remove(32)  # KeyError: 32



# 6. discard() method - Removes an element from the set
s.discard(54)
print("discard", s)

# 54 is not present in the set
s.discard(54)
print("discard", s)



# 6. pop() method - Removes an arbitrary element from the set. arbitrary means random
s.pop()
print("pop ",s)



# 8. clear() method - Removes all elements from the set and makes it empty
s.clear()
print("clear", s)



# 9. copy() method - Returns a shallow copy of the set
s = {11, 32, 54, 87, "hero", "zero", 74.12}
s1 = s.copy()
print("copy ", s1)






