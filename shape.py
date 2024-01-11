class Shape:
    def __init__(self,area):
        self.area=area

class Circle(Shape):
    def display(self,radius):
        self.radius=radius
        print("area of circle :",3.14*self.radius**2)

class Rectangle(Shape):
    def display(self,length,width):
        self.length=length
        self.width=width
        print("area of rectangle is :",length*width)
        


c=Circle(5)
c.display()

r=Rectangle(5,8)
r.display()