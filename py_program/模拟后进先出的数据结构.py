class Stack:
    def __init__(self,stack=[]):
        self.stack = []
        for x in stack:
            self.push(x)
    def isEmpty(self):
        return not self.stack
    def push(self,obj):
        self.stack.append(obj)
    def pop(self):
        if not self.stack:
            print('Stack is empty!')
        else:
            return self.stack.pop()
    def bottom(self):
        if not self.stack:
            print('Stack is empty!')
        else:
            return self.stack[0]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print('插入数字1,2,3:')
print('bottom:',s.bottom())
print('pop1:',s.pop())
print('pop2:',s.pop())
print('pop3:',s.pop())
print('isEmpty:',s.isEmpty())
