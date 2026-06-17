#this is a program to add the method of the rectangle
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        self.a = self.length * self.breadth
        print(f"the area of rectangle is: {self.a}")

    def perimeter(self):
        self.p = 2*(self.length + self.breadth)
        print(f"The perimeter is: {self.p}")

r = Rectangle(5,9)
r.area()
r.perimeter()