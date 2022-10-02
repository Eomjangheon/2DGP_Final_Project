from pico2d import*
import random
import main_state
import game_world

class Exp_jam:
    image=None
    def __init__(self):
        self.x,self.y=random.randint(0,1280),random.randint(0,800)
        self.dx,self.dy=0,0
        self.ax,self.ay=0,0
        self.count=0
        self.exp=2
        self.isEat=False
        if self.image==None:
            self.image=load_image("res/vfx/GemGreen.png")

    def update(self):
        self.x-=main_state.player.dx
        self.y-=main_state.player.dy
        if(self.isEat==False):
            if self.x<640+50 and self.x>640-50 and self.y<400+50 and self.y>400-50:
                self.isEat=True
                self.dx=(self.x-640)/5
                self.ax=-self.dx/3
                self.dy=(self.y-400)/5
                self.ay=-self.dy/3
        else:
            self.eat()

    def draw(self):
        self.image.draw(self.x,self.y)

    def eat(self):
        self.x+=self.dx
        self.y+=self.dy
        self.dx+=self.ax
        self.dy+=self.ay
        self.count+=1
        if self.count==10:
            main_state.player.exp+=self.exp
            game_world.remove_object(self)



