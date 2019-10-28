import random as r

x_range = [0,10]
y_range = [0,10]

class Turtle:
    def __init__(self):
        #初始化体力
        self.power = 100
        #初始化乌龟位置
        self.x = r.randint(x_range[0],x_range[1])
        self.y = r.randint(y_range[0],y_range[1])

    def move(self):
        turtle_x = self.x + r.choice([-2,-1,1,2])
        turtle_y = self.y + r.choice([-2,-1,1,2])
        
        #检查是否移出x轴边界
        if turtle_x < x_range[0]:
            self.x = x_range[0] - (turtle_x - x_range[0])
        elif x_range[1] < turtle_x:
            self.x = x_range[1] - (turtle_x - x_range[1])
        else:
            self.x = turtle_x
        #检查是否移出y轴边界
        if turtle_y < y_range[0]:
            self.y = y_range[0] - (turtle_y - y_range[0])
        elif y_range[1] < turtle_y:
            self.y = y_range[1] - (turtle_y - y_range[1])
        else:
            self.y = turtle_y
        #移动一次减1能量
        self.power -= 1
        #返回乌龟的位置
        return (self.x,self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        #初始化鱼位置
        self.x = r.randint(x_range[0],x_range[1])
        self.y = r.randint(y_range[0],y_range[1])

    def move(self):
        fish_x = self.x + r.choice([-1,1])
        fish_y = self.y + r.choice([-1,1])
        
        #检查是否移出x轴边界
        if fish_x < x_range[0]:
            self.x = x_range[0] - (fish_x - x_range[0])
        elif x_range[1] < fish_x:
            self.x = x_range[1] - (fish_x - x_range[1])
        else:
            self.x = fish_x
        #检查是否移出y轴边界
        if fish_y < y_range[0]:
            self.y = y_range[0] - (fish_y - y_range[0])
        elif y_range[1] < fish_y:
            self.y = y_range[1] - (fish_y - y_range[1])
        else:
            self.y = fish_y
        #返回鱼的位置
        return (self.x,self.y)

turtle = Turtle()
fish = []
for i in range(10):
    fish_site = Fish()
    fish.append(fish_site)

while True:
    if not len(fish):
        print('鱼吃完了，game over!')
        break
    elif not turtle.power:
        print('乌龟体力耗尽，game over!')
        break
    pos = turtle.move()

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            #鱼被吃了
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼被吃了')
