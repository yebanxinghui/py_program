num = input("请输入一个整数（输入Q结束程序）：")  
while num != 'Q':      
    if num.isdigit():  
        num = int(num)  
        print('十进制 -> 十六进制：%d -> %#x'%(num,num))  
        print('十进制 -> 十六进制：%d -> %#o'%(num,num))  
        print('十进制 -> 十六进制：%d ->'%num,bin(num))  
        num = input("请输入一个整数（输入Q结束程序）：")  
    else:  
        if num == 'Q':  
            break  
        else:  
            num = input("输入不合法，请输入一个整数（输入Q结束程序）：")  
