'''
Create a class 'pets' from the class 'animals' and futher create a class 'dogs' from the class 'pets'. Add a method 'bark' to the class 'dogs'.


'''


class Animals:

    def __init__(self):
        pass


class Pets(Animals):

    def __init__(self):
        super().__init__()
    
class Dogs(Pets):

    def __init__(self):
        super().__init__()

    @staticmethod
    def bark():
        print("Dog is barking!")


a = Dogs()
a.bark()