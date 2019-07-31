class Dog():

	def __init__(self, name, age): # 注意两边是两个短横线
		self.name = name
		self.age = age

	def sit(self):
		print(self.name + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + "is rolled now")


dog = Dog("xiaohu", 6)

dog.sit()
dog.roll_over()
dog.name = "ddd"
print(dog.name)
