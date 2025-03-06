'''
Write __str__ method to print the vector as follows:
7x + 8y + 10z
where x, y, z are the base vectors. 
Assume vector of 3 dimensions for this problem.

'''


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def __add__(self, other):
        
    #     result = Vector(self.x + other.x, self.y + other.y, self.z + other.z) 
    #     return result
    
    def __str__(self):
        return f"{self.x}x + {self.y}y + {self.z}z"
    

c1 = Vector(1,2,4)
# c2 = Vector(11,22,44)

print(c1)
