'''
 Create a class (2D vector) and use it to create another class (3D vector). 


'''


class TwoDVector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The two dimensional vector is {self.x}x, {self.y}y")

class ThreeDVector(TwoDVector):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The three dimensional vector is {self.x}x, {self.y}y, {self.z}z")

    
a = TwoDVector(12, 25)
a.show()

b = ThreeDVector(7, 11, 43)
b.show()
