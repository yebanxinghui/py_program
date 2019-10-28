def confict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0,nextY - i):
            return True
    return False

def queens(num = 8, state = ()):
    for pos in range(num):
        if not confict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result
#产生了一个生成器，使用for循环
for solution in queens(8):
    print(solution)
    
import random
def prettyprint(solution):
    def line(pos, length = len(solution)):
        return('. ' * (pos) + 'X ' + '. ' * (length - pos - 1))
    for pos in solution:
        print(line(pos))
prettyprint(random.choice(list(queens(8))))
