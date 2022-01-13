aliens = []
for alien_number in range(0, 30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for item in aliens[0:3]:
	if item['color'] == 'green':
		item['color'] = 'yellow'
		item['speed'] = 'medium'
		item['points'] = 10

for item in aliens[0:5]:
	print(item)

print("....")

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	'student': {
		'name': '小虎',
		'age': 20,
		'height': 170
	}
}

print("you order:" + pizza['crust'])
print("needing topping:")
for item in pizza['toppings']:
	print(item, end=",")
