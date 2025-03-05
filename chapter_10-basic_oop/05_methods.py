'''
Methods in Python
    Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
    A method is a function that belongs to an object.
    In Python, a method is a function that is available for a given object because of the object's type.
    Methods are accessed using the dot notation.
    The first argument in the method definition is always the object that is calling the method. It is passed automatically.
    Methods can operate on the data (instance variables) that is contained in the class.

'''


'''
Type of methods in python
1. Instance Method
2. Class Method
3. Static Method
4. Property Method
5. Dunder Method

1. Instance Method: Instance methods are the most common type of methods in Python classes. They are the methods that are called on an object.
2. Class Method: Class methods are the methods that are bound to the class and not the object of the class. They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
3. Static Method: A static method is also a method that is bound to the class and not the object of the class. A static method can’t access or modify class state. It is present in a class because it makes sense for the method to be present in class.
4. Property Method: Property methods are the methods that are used to get, set, and delete the values of an attribute of a class.
5. Dunder Method: Dunder methods are special methods that have double underscores at the beginning and end of their names. They are also called magic methods. They are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the __add__() method will be called.

'''