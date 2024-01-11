from abc import ABC,abstractclassmethod

#define abstract class

class shape(ABC):
    #abstract method
    def area(self):
        print("area of the shape")

    def premeter(self):
        print("premeter of the shape")

class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
