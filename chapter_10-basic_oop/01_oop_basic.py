'''
Class:
    Class is a blueprint/templete for creating objects. 
    It defines a set of attributes that will characterize any object that is instantiated from this class.
    No memory is allocated when class is created.
    Class can only be created once.
    Class is a logical entity.
    Class can be created using the keyword class.
'''

'''
Object: 
    An object is an instance of a class. 
    When class is defined, only the description for the object is defined.
    Memory is allocated only after the object is created.
    Multiple objects can be created using the same class.
    Object is a physical/real entity.
    Object can be created using the keyword new.

    Object of given class can invoke methods available to it without revealing the implementation details to the user. (Abstraction and Encapsulation)
'''


'''
Class Attributes:
    An attribute belong to the class rather than the object of the class.
    Class attributes are the attributes that are common to all the objects of the class.
    Class attributes are shared by all the objects of the class.
    Class attributes are defined outside the constructor.

'''


class employee:
    # Class Attribute
    company = "Google"
    language = "Python"
    salary = 1000000
    


# Creating object of class employee
harry = employee()

#object/instance attributes
harry.name = "Harry"
harry.age = 25

print(harry.name, harry.age, harry.language, harry.company, harry.salary)

# Creating object of class employee
rohan = employee()

#object/instance attributes
rohan.name = "Rohan"
rohan.age = 30

print(rohan.name, rohan.age, rohan.language, rohan.salary, rohan.company)