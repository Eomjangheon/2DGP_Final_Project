from pico2d import*
import random
import main_state
import game_world

class Exp_jam:
    image=None
    def __init__(self,inX,inY,inExp):
        self.x,self.y=inX,inY
        self.dx,self.dy=0,0
        self.ax,self.ay=0,0
        self.count=0
        self.exp=inExp
        self.isEat=False
        if self.image==None:
            self.image=load_image("res/vfx/GemGreen.png")

    def update(self):
        self.x-=main_state.player.dx
        self.y-=main_state.player.dy
        grabDistan=main_state.player.grabDis+main_state.player.my_skill[2]*20
        if(self.isEat==False):
            if self.x<640+grabDistan and self.x>640-grabDistan and self.y<400+grabDistan and self.y>400-grabDistan:
                self.eatSet()
            elif len(game_world.objects[1])>100:
                self.eatSet()
        else:
            self.eat()

    def draw(self):
        self.image.draw(self.x,self.y,22,28)

    def eat(self):
        self.x+=self.dx
        self.y+=self.dy
        self.dx+=self.ax
        self.dy+=self.ay
        self.count+=1
        if self.count==10:
            main_state.player.exp+=self.exp
            game_world.remove_object(self)
    def eatSet(self):
            self.isEat=True
            self.dx=(self.x-640)/5
            self.ax=-self.dx/3
            self.dy=(self.y-400)/5
            self.ay=-self.dy/3



