def main():
    list1 = [1,2,4,5,7,100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(len(list1))
    print(list1[0])
    print(list1[4])
    # print(list1[7])
    print(list1[-1])
    print(list1[-3])
    list1[2] = -1
    print(list1)
    list1.append(200)
    list1.insert(1, 400)
    print(list1)
    list1.remove(2)
    print(list1)
    if 100 in list1:
        list1.remove(100)
    print(list1)
    del list1[0]
    print(list1)
    list1.clear()
    print(list1)

if __name__=='__main__':
    main()
