favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

friends = ['phil', 'sarah']
# favorite_languages.keys() 返回的是列表
if 'xiao hu' not in favorite_languages.keys():
	print("please take in please!")

for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("hi "+ name.title() + ",I see you favorite laguages is  "+ favorite_languages[name])

print(" the follow languages have been menthond:")
for languages in favorite_languages.values():
	print(languages.title())