"""
Erkinbek
11/15/2022

Modify the code to add two additional attributes of ‘type’ and ‘manufacturer’. Then add their
corresponding methods to print those attributes, don’t forget to also modify the method
fullspecs() to return the additional attributes ‘type’ and ‘manufacturer’.
"""

class car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_color(self):
        return self.color
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_type(self):
        return self.type
    def get_manufacturer(self):
        return self.manufacturer
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacturer

car1 = car("Sports", 2020, "Blue", "Hybrid", "toyota")
car2 = car("Sedan", 2012, "Black", "Diesel", "Honda")
car3 = car("Hatchback", 2007, "Gasoline", "", "BMW")

print(car1.get_color)
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
print(car3.get_manufacturer())