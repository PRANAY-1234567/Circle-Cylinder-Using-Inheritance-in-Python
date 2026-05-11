import math

class Circle:
    def __init__(self):
        self.rad = 0

    def input_radius(self):
        self.rad = float(input("Enter the radius : "))

    def area(self):
        a = math.pi * self.rad * self.rad
        print("Area of circle :", a)

    def circumference(self):
        c = 2 * math.pi * self.rad
        print("Circumference :", c)


class Cylinder(Circle):   # Inheriting Circle class
    def __init__(self):
        super().__init__()
        self.ht = 0

    def input_height(self):
        self.ht = float(input("Enter the height : "))

    def volume(self):
        v = math.pi * self.rad * self.rad * self.ht
        print("Volume :", v)

    def surface_area(self):
        sa = 2 * math.pi * self.rad * self.ht
        print("Surface area :", sa)


class Inh3:
    @staticmethod
    def main():
        c = Cylinder()

        c.input_radius()
        c.input_height()

        print("\nBase of Cylinder")
        print("------------------------")
        c.area()
        c.circumference()

        print("\nBody of Cylinder")
        print("------------------------")
        c.volume()
        c.surface_area()


# Calling main method
Inh3.main()
