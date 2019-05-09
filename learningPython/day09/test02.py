alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] =='medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] += x_increment

print("now x-position: " + str(alien_0['x_position']))

# 字典的遍历

user_0 = {
	'username':'xiaohu',
	'first': 'enrico',
	'last': 'fermi'
	}
for key, value in user_0.items():
	print("key:{},value:{}".format(key, value), end="\t")

print()
for key in user_0.keys():
	print("key", key)

