def sum(x):
    result = 0
    for i in x:
        if type(i) == int or type(i) == float:
            result += i
        else: continue
    return result
print(sum([1,2.1,'true']))
