class Distance_Conversion:
    def __init__(self, meter):
        self.meter = meter
    def Centimeter(self):
        return self.meter * 100
    def Kilometer(self):
        return self.meter / 1000
    def Inches(self):
        return self.meter * 39.37
    def result(self):
        print("Centimeters: ", round(self.meter(), 100))
        print("Kilometers: ", round(self.perimeter(), 1000))
        print("Inches: ", round(self.meter(), 39.37))


m=int(input("Enter the distance in meters: "))

obj=Distance_Conversion(m)

print("Meters to Centimeters: ", obj.Centimeter(), )
print("Meters to Kilometers: ", obj.Kilometer(), )
print("Meters to Inches: ", obj.Inches(), )

