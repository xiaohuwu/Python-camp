alien_0 = {'color': 'green', 'points': 34}
alien_1 = {'color': 'green', 'points': 34}
alien_2 = {'color': 'green', 'points': 34}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

aliens = []
for alien_number in range(1, 31):
	new_alien = {'color': 'green', 'points': 34}
	aliens.append(new_alien)

print("...")
for alien in aliens[0:5]:
	print(alien)

print("...")
print("Total number of aliens: "+str(len(aliens)))


