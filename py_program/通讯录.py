print(""" 
|--- 欢迎进入通讯录程序 ---| 
|---  1：查询联系人资料 ---| 
|---  2：插入新的联系人 ---| 
|---  3：删除已有联系人 ---| 
|---  4：退出通讯录程序 ---|""")  
  
key = 5  
dict1 = {'小甲鱼':'020-88974651'}  
while key != 4:  
    key = int(input('请输入相关的指令代码：'))  
    if key == 1:  
        temp = input('请输入联系人姓名：')
        if temp in dict1:
            print('%s : %s\n'%(temp,dict1[temp]))  
        else:
            print('您输入的姓名不在通讯录中\n ')  
    elif key == 2:  
        temp = input('请输入联系人姓名：')          
        if temp in dict1:  
            print('您输入的姓名已在通讯录中存在 --> %s:%s'%(temp,dict1[temp]))  
            x = input('是否修改用户资料(YES/NO)')  
            if x == 'YES':  
                tel = input('请输入用户联系电话：')  
                dict1.update({temp:tel})  
                print('修改后的联系人的资料为：%s --> %s\n'%(temp,dict1[temp]))  
        else:  
            temp1 = input('请输入联系人电话：')  
            dict1[temp] = temp1  
            print('添加的联系人的资料为：%s --> %s\n'%(temp,dict1[temp]))  
    elif key == 3:  
        temp = input('请输入要删除的联系人姓名：')  
        if temp in dict1:  
            flag = input('确定要删除此联系人?(YES/NO)')  
            if flag == 'YES':  
                del(dict1[temp])  
                print('联系人 %s 删除成功\n！'%temp)  
            else:  
                continue  
        else:  
            print('%s 不在通讯录中\n '%temp)  
    elif key == 4:  
        print("|--- 感谢使用通讯录程序 ---|")  
        break  
    else:
        print('指令不正确！请重新输入！\n')
