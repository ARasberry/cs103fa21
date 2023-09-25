def fibonacci(n):
    print(0)
    f1, f2 = 0, 1
    x = 0
    for i in range(n-1):
        f1 = f2
        f2 = x
        x = f1 + f2
        print(x)


fibonacci(5)

