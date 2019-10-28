class C:
    def __init__(self, *args):
        if not args:
            print('没有传入参数')
        else:
            print('传入了 %d 个参数' % len(args))
            print('这些参数分别是:', end = '')
            for each in args:
                print(each, end = ' ')
c1 = C()

c2 = C(1, 2, 3)
