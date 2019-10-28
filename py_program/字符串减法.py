class Nstr(str):
    def __sub__(self,other):
        return self.replace(other,'')
a = Nstr('123aaa')
b = Nstr('a')
print(a - b)
