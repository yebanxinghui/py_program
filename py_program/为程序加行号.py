import fileinput

for line in fileinput.input(): #如果需要原地操作，那么就加个参数inplace = True
    line =line.rstrip()
    num = fileinput.lineno()
    print('%-40s # %2i' % (line, num))
