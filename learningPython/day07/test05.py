def item( num ):
    if num == 0 :
        return 0
    elif num == 1:
        return 1
    else:
        return item ( num - 1) + item (num -2)


def fibo(no):
	i = 0
	while i < no:
		print(item(i))
		i += 1

fibo(20)