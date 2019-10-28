class Nstr:
    def __init__(self, arg = ''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print('参数错误')
    def __add__(self, other):
        return self.total + other.total
    def __sub__(self, other):
        return self.total - other.total
    def __mul__(self, other):
        return self.total * other.total
    def __truediv__(self, other):
        return self.total / other.total
    def __floordiv__(self, other):
        return self.total // other.total
a = Nstr('FishC')
b = Nstr('love')
print(a + b, a - b, a * b, a / b, a // b)
