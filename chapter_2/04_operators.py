# -------------------------Arthemetic Operators in Python-------------------------
print("Arthemetic Operators in Python")
print("5 + 3 =", 5 + 3) # Addition
print("5 - 3 =", 5 - 3) # Subtraction
print("5 * 3 =", 5 * 3) # Multiplication
print("5 / 3 =", 5 / 3) # Division
print("\n")

# -------------------------Assignment Operators in Python-------------------------

print("Assignment Operators in Python")
a = 5
b = 3
print("a =", a)
print("b =", b)

a += 3 # a = a + 3
b -= 3 # b = b - 3
print("a += 3", a)
print("b -= 3", b)

a *= 3 # a = a * 3
b /= 3 # b = b / 3
print("a *= 3", a)
print("b /= 3", b)
print("\n")

# -------------------------Comparison Operators in Python-------------------------
print("Comparison Operators in Python")
a = 5
b = 3
c = 5

print("a == b", a == b) # False
print("a == c", a == c) # True
print("a > b", a > b) # True
print("a < b", a < b) # False
print("a >= b", a >= b) # True
print("a <= b", a <= b) # False
print("a != b", a != b) # True
print("\n")

# -------------------------Logical Operators in Python-------------------------
print("Logical Operators in Python")
a = True
b = False

print("a and b :", a and b) # False
print("a or b :", a or b) # True
print("not a :", not a) # False
print("not b :", not b) # True
print("\n")

# truth table for "and" operator
print("Truth table for 'and' operator")
print("True and True :", True and True) # True
print("True and False :", True and False) # False
print("False and True :", False and True) # False
print("False and False :", False and False) # False
print("\n")

# truth table for "or" operator
print("Truth table for 'or' operator")
print("True or True :", True or True) # True
print("True or False :", True or False) # True
print("False or True :", False or True) # True
print("False or False :", False or False) # False
print("\n")

print("Truth table for 'not' operator")
# truth table for "not" operator
print("not True :", not True) # False
print("not False :", not False) # True
print("\n")

# -------------------------Bitwise Operators in Python-------------------------

print("Bitwise Operators in Python")
a = 5
b = 3

print("a & b :", a & b) # 1 - bitwise and
print("a | b :", a | b) # 7 - bitwise or
print("a ^ b :", a ^ b) # 6 - bitwise xor
print("~a :", ~a) # -6 - bitwise not
print("a << 1 :", a << 1) # 10 - right shift
print("a >> 1 :", a >> 1) # 2 - left shift
print("\n")

# -------------------------Identity Operators in Python-------------------------

print("Identity Operators in Python")

a = 5
b = 5
c = 3

print("a is b :", a is b) # True - a and b are same objects
print("a is c :", a is c) # False - a and c are different objects
print("a is not b :", a is not b) # False - a and b are same objects
print("a is not c :", a is not c) # True - a and c are different objects
