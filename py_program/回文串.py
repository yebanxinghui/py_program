def huiwen():
    s = input('input a string: ')
    len1 = len(s)
    i = 0
    j = len1 - 1
    len2 = j // 2
    while i<=j and s[i] == s[j]:
        i += 1
        j -= 1
    if i - 1 == len2:
        print('%s 是回文联！' % s)  
    else :
        print('%s 不是回文联！' % s)
huiwen()
