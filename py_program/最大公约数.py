def gcd1(x,y):
    while x:
        if x < y:
            x,y = y,x
        x = x % y
    return y

def gcd2(x,y):  
    while y:  
        t = x%y  
        x = y  
        y = t  
    return x

#递归法
def gcd3(x, y):  
    if y:  
        return gcd3(y, x%y)  
    else:  
        return x
    
 
print(gcd1(14,21))
print(gcd2(16,18))
print(gcd3(8,12))
