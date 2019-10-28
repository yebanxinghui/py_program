#密码安全性检查代码  
#  
#低级密码要求：  
# 1.密码由单纯的数字或字母组成  
# 2.密码长度小于等于8位  
#  
#中级密码要求：  
# 1.密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}\|）任意两种组合  
#密码长度不能低于8位  
#  
#高级密码要求：  
# 1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}\|）三种组合  
# 2.密码只能由字母开头  
# 3.密码长度不能低于16位  
  
str1 = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"  
has_str1 = 0  
has_num = 0  
has_alpha = 0  
t = 'y'  
while t == 'y':  
        password = input("请输入需要检查的密码组合：")  
        length = len(password)  
        while(password.isspace() or length == 0):  
                password = input('您输入的密码为空（或空格），请重新输入：')  
        for i in password:  
                if i in str1:  
                        has_str1 = 1  
                if i.isdigit():  
                        has_num = 1  
                if i.isalpha():  
                        has_alpha = 1  
        has =  has_str1 + has_num + has_alpha  
        if length <= 8 or password.isalnum():  
                level = "低"  
        if length > 8 and has ==2:  
                level = "中"  
        if length >= 16 and has == 3 and password[0].isalnum():  
                level = "高"  
        print("您的密码安全等级评定为：%s"%level)  
        if level == "高":  
                print("请继续保持")  
        else:  
                print("""请按以下方式提升您的密码安全级别： 
        1.密码必须由数字、字母及特殊字符三种组合 
        2.密码只能由字母开头 
        3.密码长度不能低于16位""")  
        t = input("还要再测试么？（”y“继续，其他退出）")  
