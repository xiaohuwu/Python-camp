# coding=utf-8
from car import Car

class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super(manufacturer, model, year)
        self.battery = Battery()


car = ElectricCar("长春", "手动", 12)
# print(car.get_descriptive_name())

