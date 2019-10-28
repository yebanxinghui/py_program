from tkinter import *
import random
import time

#我们的弹球类
class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        #使每次小球开始弹的方向不一样
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        #控制游戏输赢
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    #判断小球是否击中球拍
    def hit_paddle(self, pos,):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                #记录得分
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False
    #控制小球移动
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        #控制球的竖直方向不会出屏幕外
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        #控制球的水平方向不会出屏幕外
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
#我们的球拍类
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        #初始化使游戏暂时不会开始
        self.started = False
        #按左右方向键移动球拍
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<Button-1>',self.start_game)
    #球拍移动
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        #控制球拍不出边界
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    #球拍的向左移动速率
    def turn_left(self,evt):
        self.x = -3
    #球拍的向右移动速率
    def turn_right(self,evt):
        self.x = 3
    #游戏延时开始
    def start_game(self,evt):
        self.started = True

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450,10,text = self.score, fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id,text = self.score)

tk=Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width = 500,height = 400,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()

score = Score(canvas,'green')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas,paddle,score, 'red')
game_over_text = canvas.create_text(250,200,text = 'GAME OVER',state = 'hidden')

#重画屏幕，不断更新屏幕
while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text,state = 'normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

