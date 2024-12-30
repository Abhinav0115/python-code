'''
Q. What will be the length of the following set s:
    s = set()
    s.add(20)
    s.add(20.0)
    s.add("20")

'''
# Solution: length will be 2


s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)
print(len(s))
