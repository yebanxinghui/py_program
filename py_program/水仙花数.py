for num in range(100,1000):
    a = num // 100
    b = (num//10) % 10
    c = num % 10
    if (a**3+b**3+c**3) == num:
        print(num,end=' ')
