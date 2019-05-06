

def fib(num):
    a = 0
    b = 1
    i = 0
    while i < num:
        print(b)
        a, b = b, a+b
        i += 1
        
fib(20)

