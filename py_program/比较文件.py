def file_compare(file1,file2):
    count = 0 #统计行数
    differ = [] #统计不相同的行数
    f1 = open(file1)
    f2 = open(file2)
    for line1 in f1:
        count += 1
        line2 = f2.readline()
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ

file1 = r'D:\text\101.txt' #如果需要，则改为input
file2 = r'D:\text\102.txt' #如果需要，则改为input

differ = file_compare(file1,file2)

print('两个文件共有 %d 处不同' % len(differ))

for i in differ:
    print('第 %d 行不同' % i)
