'''
Class Method:
    - Class method is a method that is bound to the class and not the object of the class.
    - They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    - It can modify the class state that would apply across all the instances of the class.
    - It can be called on the class or on the instance of the class.
    - It is defined using the @classmethod decorator.
    syntax:
        @classmethod
        def class_method(cls, arg1, arg2, ...):
            pass
'''


'''
'''


class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    def show_obj(cls):
        print(f"the instance attribute of a is {cls.a}")
    

e = Employee()
e.a = 14

e.show()
e.show_obj()
