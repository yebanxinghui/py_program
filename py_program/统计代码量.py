import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ''
    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "【%s】源文件%d个，源代码%d行\n" % (i, file_list[i],lines)
    title = '统计结果'
    msg = '你目前一共编写了%d行代码，完成进度: %0.2f %%\n离10万行代码还差%d行，请继续努力！' % (total,total/1000,100000-total)
    g.textbox(msg, title, text)

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件: %s ...' % file_name)
        try:
            for each in f:
                lines += 1
        except UnicodeDecodeError:
            pass #防止遇到格式不兼容的文件
    return lines

def search_file(start_dir):
    os.chdir(start_dir)

    for each in os.listdir(os.curdir):
        ext = os.path.splitext(each)[1]
        if ext in target:
            lines = calc_code(each) #统计行数
            #统计文件数 
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            #统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
        if os.path.isdir(each):
            search_file(each) #递归调用
            os.chdir(os.pardir) #递归调用后返回上一层目录

target = ['.c','.cpp','.py','.cc','.java','.pas','.asm']
file_list = {}
source_list = {}

g.msgbox('请打开您存放所用代码的文件夹...','统计代码量')
path = g.diropenbox('请选择你的代码库:')

search_file(path)
show_result(path)
