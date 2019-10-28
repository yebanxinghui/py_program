import easygui as g
import random as r
g.msgbox('欢迎进入猜数小游戏：','猜数小游戏','game start->')

number = r.randint(1,10)
guess = g.integerbox('不放猜一下小甲鱼心里想的什么数字(1-10):','数字小游戏',lowerbound = 1, upperbound = 10)

while True:
    if number == guess:
        g.msgbox("斯国一，然后真遗憾，猜中了也没有奖励！")
        break
    else:
        if guess > number:
            g.msgbox("大了大了~~~")
        else:
            g.msgbox("小了小了~~~")
        guess = g.integerbox('继续猜猜看', '再接再厉', lowerbound=1, upperbound=10)
g.msgbox("游戏结束，不玩啦^_^")