import os
all_files = os.listdir(os.curdir)
dict1 = dict()

for each_file in all_files:
    if os.path.isfile(each_file):
        dict1.setdefault(each_file, os.path.getsize(each_file))
        print('%s 的大小是 %d Bytes' % (each_file, dict1[each_file]))
