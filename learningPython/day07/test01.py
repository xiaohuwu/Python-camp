def main():
    str1 = 'hello world'
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find("or"))
    print(str1.center(50, '*'))
    print(str1.rjust(50,"*"))
    print(str1[2:])
    print(str1[::2])
    print(str1[-3:-1])
if  __name__ == '__main__':
    main()
