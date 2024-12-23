#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14159 * (self.radius ** 2)

    def calculatePerimeter(self):
        return 2 * 3.14159 * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Area of the circle: {circle.calculateArea():.2f}")
print(f"Perimeter of the circle: {circle.calculatePerimeter():.2f}")

#math function can also be imported for value of pie
