aliens = []
for alien_number in range(0,30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for item in aliens[0:3]:
	if item['color'] =='green':
		item['color'] = 'yellow'
		item['speed'] = 'medium'
		item['points'] = 10

for item in aliens[0:5]:
	print(item)

print("....")
