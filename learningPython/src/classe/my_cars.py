# from electric_car import *   # 导入模块里面的所有类 或方法
import electric_car  # 导入模块 访问的时候 需要模块名加方法

my_beetle = electric_car.Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.get_descriptive_name())
