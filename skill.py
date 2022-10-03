from pico2d import*
import random
import main_state
import math
import game_world


class Skill:
    def __init__(self):
        pass
    def update(self):
        self.x-=main_state.player.dx
        self.y-=main_state.player.dy
        self.x+=self.dx
        self.y+=self.dy
        if (self.x>1280 or self.x<0 or self.y<0 or self.y>800):
            game_world.remove_object(self)

    
    
class FireBall(Skill):
    image=None
    def __init__(self,s_lv):
        #나중에 게임매니저에서 관리한다
        self.w,self.h=31,16
        self.x,self.y=640,400
        self.lv=s_lv
        self.damage=s_lv*2
        self.dx=random.randint(-100,100)/100
        self.dy=random.randint(-100,100)/100
        if self.dx==0:
            self.dx=0.00000001
            
        self.theta=math.atan(self.dy/self.dx)
        if(self.dx<0):
            self.theta+=math.pi
        self.dx=math.cos(self.theta)*5
        self.dy=math.sin(self.theta)*5
        
        if self.image==None:
            self.image=load_image("res/vfx/fireball.png")
            
    def draw(self):
        self.image.clip_composite_draw(0, 0, self.w, self.h, self.theta, '', self.x, self.y, self.w*self.lv, self.h*self.lv)




