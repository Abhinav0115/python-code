'''
Property Decorators:
    - Property Decorators allows us to define a method that we can access like an attribute.
    - It allows us to define a method that can be accessed like an attribute.
    - It is defined using the @property decorator.
    syntax:
        @property
        def attribute(self):
            pass
            
'''

'''
Types of Property Decorators:
    - Getter
    - Setter
    - Deleter

Getter:
    - It is used to get the value of the attribute.
    - It is defined using the @property decorator.
    syntax:
        @property
        def attribute(self):
            pass

Setter:
    - It is used to set the value of the attribute.
    - It is defined using the @attribute.setter decorator.
    syntax:
        @attribute.setter
        def attribute(self, value):
            pass
            
Deleter:
    - It is used to delete the value of the attribute.
    - It is defined using the @attribute.deleter decorator.
    syntax:
        @attribute.deleter
        def attribute(self):
            pass
            

'''


class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(' ')[0]
        self.lname = value.split(' ')[1]
    

e = Employee()
e.a = 14

e.show()
e.name = 'John Doe'

print(e.fname, e.lname)
print(e.name)



