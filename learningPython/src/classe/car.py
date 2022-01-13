# coding=utf-8
class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) +" " + self.manufacturer + " " + self.model
        return long_name.title()

    def setValue(self,odometer):
        self.odometer = odometer

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it")

    def update_odometer(self, miles):
        self.odometer += miles


car = Car("长春", '手动', 12)
car.read_odometer()
car.update_odometer(12)
car.read_odometer()

