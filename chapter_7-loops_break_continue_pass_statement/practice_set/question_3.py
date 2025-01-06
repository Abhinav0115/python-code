'''
Q. Write a program to greet all the person names stored in a list l1 and which starts with S.
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

'''

l1 = ["Harry", "Sohan", "Sachin", "Rahul"]


for name in l1: 
    if(name.lower().startswith("s")):
        print(f"Hello, {name}")


