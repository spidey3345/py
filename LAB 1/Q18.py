#Implement a class Shape with a method area() which returns 0. Then, create subclasses Rectangle and Circle. Overload the area() method in both subclasses to calculate and return the area of a rectangle and a circle respectively.

class Shape():
    def area(self):
        return(0)

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
       return self.length*self.breadth
 
   
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14159 * (self.radius ** 2)

shape = Shape()
print(f"Area of Shape: {shape.area()}")  

rectangle = Rectangle(5, 10)
print(f"Area of Rectangle: {rectangle.area()}")

circle = Circle(7)
print(f"Area of Circle: {circle.area()}") 
