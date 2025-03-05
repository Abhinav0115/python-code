'''
Class Attributes  vs Instance Attributes:

Class Attributes:
    An attribute belong to the class rather than the object of the class.
    Class attributes are the attributes that are common to all the objects of the class.
    Class attributes are shared by all the objects of the class.
    Class attributes are defined outside the constructor.

Instance Attributes:
    An attribute that belongs to the object.
    Instance attributes are unique to each object.
    Instance attributes are not shared by other objects.
    Instance attributes are defined inside the constructor.

'''

'''
Instance Attributes take precedence over Class Attributes i.e. if an instance attribute and class attribute have the same name, instance attribute will be used.

If we try to access an attribute of an object, it first checks if the attribute is present in the object. If it is not present in the object, it checks if the attribute is present in the class of that object. If it is present in the class, it returns the value of the attribute of the class. If it is not present in the class, it returns an error.

'''



class employee: 
    salary = 100000       # Class attributes
    language =  "python"  # Class attributes


print(employee.salary, employee.language) # Class attributes are shared by all the objects of the class.

harry = employee()
harry.name = "harry"     # Instance attribute
harry.language = "java"  # Instance attribute
harry.salary = 200000    # Instance attribute

print(harry.name, harry.language, harry.salary)

rohan = employee()
rohan.name = "rohan"    # Instance attribute
rohan.language = "c++"  # Instance attribute

print(rohan.name, rohan.language, rohan.salary)
