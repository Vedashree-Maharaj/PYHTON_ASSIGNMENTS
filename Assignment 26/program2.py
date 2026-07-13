# Program to implement a class Circle

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the Radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle:", self.Radius)
        print("Area of Circle:", self.Area)
        print("Circumference of Circle:", self.Circumference)


cobj = Circle()

cobj.Accept()
cobj.CalculateArea()
cobj.CalculateCircumference()
cobj.Display()