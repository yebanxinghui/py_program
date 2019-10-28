def get_digit(n):
    result = ''
    if n:
        result = get_digit(n//10)
        result += str(n%10)
    return list(result)

num = int(input('请输入一个数：'))  
print(get_digit(num))
