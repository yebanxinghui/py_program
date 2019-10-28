import easygui as g
import sys
fields = ('*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail')
while True:
    temp = g.multenterbox("【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。\n","账号中心",fields)
    if temp == None:
        sys.exit(0)
    for i in range(len(temp)):
        errmsg = ""
        if fields[i][0] == '*' and temp[i].strip() == '':
            errmsg += ('【%s】为必填项。\n' % fields[i])
            g.msgbox(errmsg, '输入错误')
            break
    else:
        g.msgbox('录入完毕','录入成功')
        break

