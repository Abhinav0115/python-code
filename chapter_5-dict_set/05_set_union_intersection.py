# 05. Set Union and Intersection

# 1. union() method - Returns a set containing the union of sets
s1 = {11, "zero", 74.12}
s2 = {11, "zero", 74.12, 100, 22}
print("union", s1.union(s2)) # This will return the union (combination) of s1 and s2. It will remove the duplicate element


# 2. intersection() method - Returns a set, that is the intersection of two other sets
s1 = {11, "zero", 74.12}
s2 = {11, "zero", 74.12, 100, 22}
print("intersection", s1.intersection(s2)) # This will return the intersection of s1 and s2. It will return the common element from both set


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 2, 3}

# 1. intersection() method - Returns a set, that is the intersection of two other sets
print("intersection ", a.intersection(b)) # This will return the common element between s1 and s2


# 2. union() method - Return a set containing the union of sets
print("union ", a.union(b)) # This will return the all element of s1 and s2


# 3. subset() method - Returns whether another set contains this set or not
print("subset ", a.issubset(b)) # This will return False because s1 is not subset of s2
print("subset", c.issubset(a)) # This will return True because s3 is subset of s1


# 4. superset() method - Returns whether this set contains another set or not
print("superset ", a.issuperset(b)) # This will return False because s1 is not superset of s2
print("superset", a.issuperset(c)) # This will return True because s1 is superset of s3


# 5. isdisjoint() method - Returns whether two sets have a intersection or not
print("isdisjoint ", a.isdisjoint(b)) # This will return False because s1 and s2 have common element