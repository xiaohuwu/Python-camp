nubmer = int(input("please input number: "))
if nubmer % 10 == 0:
	print(" can divied 10")
else:
	print(" can not devied 10")
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_user = []


print(unconfirmed_users)

while unconfirmed_users:
	user = unconfirmed_users.pop(-1)
	confirmed_user.append(user)

print("The following users have been confirmed:")
print(confirmed_user)
