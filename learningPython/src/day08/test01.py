class Student(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

# 如果希望属性私有 可以设置下滑线
	def __study(self,course_name):
		print("{}正在学习{}".format(self.name,course_name))

	def watch(self):
		if self.age < 18:
			print( "{}只能观看熊出没".format(self.name) )
		else:
			print( "{}可以看其他的".format(self.name) )


def main():
	stu1 = Student('罗浩',38)
	stu1._Student__study("Python 程序设计")
	stu1.watch()



if __name__=='__main__':
	main()