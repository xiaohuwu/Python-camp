pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
	index = pets.index('cat')
	pets.pop(index)
	print(pets)
response = {}
polling_active = True
while polling_active:
	name = input("\n what is you name: ")
	mountain = input("\n mountain you like: ")
	response[name] = mountain
	polling_active = input("more answer:").lower() == 'yes'

print("result:")
for name, mountain in response.items():
	print(name + "like climb" + mountain + ".")
