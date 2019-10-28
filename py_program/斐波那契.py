
#递归法用列表
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
num=int(input('how many Fibonacci numbers do you want? '))
a=fibs(num)
print(a)
print(a[-1])

#递归法不用列表
'''
def fibs(n):
    if n < 1:
        print('输入有误')
    if n==1 or n==2:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)
num=int(input('how many Fibonacci numbers do you want? '))
a=fibs(num)
print(a)
'''

#迭代法
'''
def fibs(n):
    n1 = 1
    n2 = 1
    n3 = 1
    while n > 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3
n = int(input('how many Fibonacci numbers do you want? '))
result = fibs(n)
print(result)
'''
