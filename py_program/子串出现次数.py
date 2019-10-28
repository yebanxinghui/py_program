def findstr1():
    count = j = 0
    string = input('请输入目标字符串：')
    ch = input('请输入子字符串（两个字符）：')
    len1=len(string)
    len2=len(ch)
    for i in range(0,len1):
        while i+j<len1 and ch[j] == string[i+j]:
            if j == len2 - 1 :
                count += 1
                j = 0
                break
            j += 1
    print('子字母串在目标字符串中共出现%d次' % count)
findstr1()
'''
def findstr2():  
    print('请输入目标字符串：',end='')  
    temp = input()  
    print('请输入子字符串（两个字符）：',end='')  
    comp = input()  
    count = 0  
    i = 0  
    for i in range(len(temp)):  
        if temp[i] == comp[0] and temp[i+1] == comp[1]:  
            count += 1  
            i += 1  
        else:  
            i += 1  
    count = int(count)  
    print('子字符串在目标字符串中总共出现 %d 次'%count)
'''
'''
findstr2()  
def findStr3(desStr, subStr):  
    count = 0  
    length = len(desStr)  
    if subStr not in desStr:  
        print('在目标字符串中未找到字符串!')  
    else:  
        for each1 in range(length):        
            if desStr[each1] == subStr[0]:  
                if desStr[each1+1] == subStr[1]:  
                    count += 1  
                      
        print('子字符串在目标字符串中共出现 %d 次' % count)  
   
desStr = input('请输入目标字符串：')  
subStr = input('请输入子字符串(两个字符)：')  
findStr3(desStr, subStr)
'''
