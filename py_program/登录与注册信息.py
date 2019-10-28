def Load():  
    dict1 = {'小甲鱼':'FishC'}  
    while 1:  
        key = input('''
|--- 新建用户：N/n ---| 
|--- 登录帐号：E/e ---| 
|--- 退出程序：Q/q ---| 
|--- 请输入指令代码：''')  
        if key == 'N' or key == 'n':  
            temp_name = input('请输入用户名：')  
            while temp_name in dict1:  
                temp_name = input('此用户名已经被使用，请重新输入：')  
            while True:
                temp_password = input('请输入密码：')
                temp_password1 = input('请重新输入再次确定密码：')
                if temp_password == temp_password1: break
                else : print('两次输入密码不一致！请重新输入！')
            dict1[temp_name] = temp_password  
            print('注册成功，赶紧试试登录吧 ^_^ ')  
            continue  
  
        elif key == 'E' or key == 'e':  
            temp_name = input('请输入用户名:')  
            while temp_name not in dict1:  
                temp_name = input('您输入的用户名不存在，请重新输入：')  
            temp_password = input('请输入密码：')  
            while temp_password != dict1[temp_name]:  
                temp_password = input('密码错误，请重新输入：')  
            print('欢迎进入系统，结束程序请点右上角的X！')  
            continue  
  
        elif key == 'Q' or key == 'q':  
            break    
Load()  
