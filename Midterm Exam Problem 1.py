class Circle():

    def radius(self, radius):
        radius = radius

    def diameter(self, diameter):
        diameter = diameter

    def area(self, diameter):
        area = (diameter / 2) ^ 2 * 3.14
        print("Area of the circle is: ", area)

    def peri(self, d):
        peri = 3.14 * radius
        print("Perimeter of the circle is: ", perimeter)

    def area(self, radius):
        area = 3.14 * radius * radius
        print("Area of the circle is: ", area)

    def perimeter(self, radius):
        perimeter = 2 * 3.14 * radius
        print("Perimeter of the circle is: ", perimeter)


c = Circle()
radius = int(input("Enter Radius: "))
diameter = int(input("Enter Enter Diameter: "))
c.area(radius)
c.perimeter(radius)
c.area(diameter)
c.perimeter(diameter)