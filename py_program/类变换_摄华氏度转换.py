class C2F(float):
        def __new__(cls, arg = 0.0):
                return float.__new__(cls, arg * 1.8 + 32)
a = C2F(10)
print(a)
