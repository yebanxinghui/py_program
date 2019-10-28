def DectoBin(num):  
    temp = []  
    result = ''  
    while num:  
        x = num%2  
        num = num//2  
        temp.append(x)  
    while temp:  
        result += str(temp.pop())  
    return result

#递归法
def Bin(n):  
    temp = ''  
    if n:  
        temp = Bin(n//2)  
        temp += str(n%2)  
        return temp  
    else:  
        return temp          
  
num = int(input('input a number: '))
print(DectoBin(num))
print(Bin(num))
