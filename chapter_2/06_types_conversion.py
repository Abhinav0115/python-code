

a = "31.2"
print(a)  # 31.2    
print(type(a))  # <class 'str'>

# type conversion from string to float
b = float(a)
print(b)  # 31.2
print(type(b))  # <class 'float'>

# type conversion from float to int
c = int(b)
print(c)  # 31
print(type(c))  # <class 'int'>

# type conversion from int to string
d = str(c)
print(d)  # 31
print(type(d))  # <class 'str'>

#Error as string is not a number
e= "Hello, World!"
print(e)  # Hello, World!
print(type(e))  # <class 'str'>

#Error as string is not a number
f = float(e)
print(f)  # ValueError: could not convert string to float: 'Hello, World!'
