def min(x):
    least = x[0]
    for each in x:
        if each < least:
            least = each
        else:
            continue
    return least
a = input('input a sequence: ')
print(min(a))
