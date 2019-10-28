count = 3
password = '2333'
while count:
    passwd=input('请输入四位数字密码:')
    if passwd == password:
        print('密码通过')
        break
    elif '*' in passwd:
        print('密码中含*号,你还有%d次机会' % count)
        continue
    else:
        print('密码错误,你还有%d次机会' % count)
    count -=1
