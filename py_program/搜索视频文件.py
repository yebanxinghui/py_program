import os  
vedio_list = []  
def search_file(start_dir) :  
    os.chdir(start_dir)     
    for each_file in os.listdir(os.curdir) :  
        if os.path.isfile(each_file) :  
            file_ext = os.path.splitext(each_file)[1]  
            if file_ext in ['.mp4','.rmvb','.avi']:  
                vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  
        elif os.path.isdir(each_file) :  
            search_file(each_file) # 递归调用  
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录  
    return vedio_list;  
  
start_dir = input('请输入待查找的初始目录：')  
vedio_list = search_file(start_dir)  
f = open(os.getcwd() + os.sep + 'VedioList.txt','w')  
f.writelines(vedio_list)  
f.close()  
