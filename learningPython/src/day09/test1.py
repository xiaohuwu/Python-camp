dimensions = (200, 500)
print(dimensions[0])
# dimensions[0] = 2 # not allowed to modify

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

