def describle_pet(pet_name, anlimal_type='dog'):
	print("\n I have a " + anlimal_type + ".")
	print("My " + anlimal_type + "'s name is " + pet_name.title() + ".")


# 位置 实参
describle_pet('大白鹅')

# 关键字实参
describle_pet(pet_name='大白鹅', anlimal_type="鸭子")


def get_full_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = str(first_name).title() + "" + middle_name + " " + last_name
	else:
		full_name = str(first_name).title() + " " + last_name
	return full_name.title()

musician = get_full_name('jimi', 'hendrix')
print(musician)

musician = get_full_name('john', 'hooker', 'lee')
print(musician)