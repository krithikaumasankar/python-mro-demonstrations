import math


# Base Class
class Shapes:
    def calculate_area(self):
        print("Area calculation")

    def calculate_perimeter(self):
        print("Perimeter calculation")


# Circle Class
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        print("Area of Circle =", area)

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("Perimeter of Circle =", perimeter)


# Rectangle Class
class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print("Area of Rectangle =", area)

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print("Perimeter of Rectangle =", perimeter)


# Triangle Class
class Triangle(Shapes):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print("Area of Triangle =", area)

    def calculate_perimeter(self):
        perimeter = self.a + self.b + self.c
        print("Perimeter of Triangle =", perimeter)


# ---------------- MAIN PROGRAM ---------------- #

print("===== Circle Details =====")
radius = float(input("Enter radius of Circle: "))
circle = Circle(radius)

print("\n===== Rectangle Details =====")
length = float(input("Enter length of Rectangle: "))
breadth = float(input("Enter breadth of Rectangle: "))
rectangle = Rectangle(length, breadth)

print("\n===== Triangle Details =====")
a = float(input("Enter side 1 of Triangle: "))
b = float(input("Enter side 2 of Triangle: "))
c = float(input("Enter side 3 of Triangle: "))
triangle = Triangle(a, b, c)


# Circle Operations
print("\n===== Circle Calculations =====")
circle.calculate_area()
circle.calculate_perimeter()

# Rectangle Operations
print("\n===== Rectangle Calculations =====")
rectangle.calculate_area()
rectangle.calculate_perimeter()

# Triangle Operations
print("\n===== Triangle Calculations =====")
triangle.calculate_area()
triangle.calculate_perimeter()


# MRO Tracing
print("\n===== MRO Tracing =====")

print("\nCircle MRO:")
for cls in Circle.mro():
    print(cls.__name__)

print("\nRectangle MRO:")
for cls in Rectangle.mro():
    print(cls.__name__)

print("\nTriangle MRO:")
for cls in Triangle.mro():
    print(cls.__name__)
