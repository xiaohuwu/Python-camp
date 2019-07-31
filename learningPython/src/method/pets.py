def describe_pet(pet_name, anlimal_type="dog"):
	print("\n I have a " + anlimal_type + ".")
	print("My " + anlimal_type + "'s name is " + pet_name.title() + ".")


# describe_pet("鸭子","小黄鸭") 位置实参


describe_pet("鸭子",anlimal_type="dog123") # 位置实参 和关键字混用


