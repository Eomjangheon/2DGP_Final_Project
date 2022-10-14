from pico2d import*
import random
import main_state
import math
import game_world


class Skill:
    def __init__(self):
        self.x,self.y=640,400
        self.dx=random.randint(-100,100)
        self.dy=random.randint(-100,100)
        if(len(game_world.objects[3])>0):
            self.target=random.randint(0,len(game_world.objects[3])-1)
            self.dx=game_world.objects[3][self.target].x-640
            self.dy=game_world.objects[3][self.target].y-400
    

    
    
class FireBall(Skill):
    name='fireball'
    image=None
    def __init__(self,s_lv):
        super().__init__()
        self.lv=s_lv
        self.w,self.h=31*self.lv,16*self.lv
        self.damage=s_lv*5+(main_state.player.my_skill[3]*2)
        self.speed=5

        if self.dx==0:
            self.dx=0.00000001
        self.theta=math.atan(self.dy/self.dx)
        if(self.dx<0):
            self.theta+=math.pi
        self.dx=math.cos(self.theta)*self.speed
        self.dy=math.sin(self.theta)*self.speed
        if self.image==None:
            self.image=load_image("res/vfx/fireball.png")
            
    def update(self):
        self.x-=main_state.player.dx
        self.y-=main_state.player.dy
        self.x+=self.dx
        self.y+=self.dy
        if (self.x>1280 or self.x<0 or self.y<0 or self.y>800):
            game_world.remove_object(self)
    
    def draw(self):
        self.image.clip_composite_draw(0, 0, self.w, self.h, self.theta, '', self.x, self.y, self.w, self.h)

class Whip(Skill):
    name='whip'
    image=None
    def __init__(self,s_lv,num):
        super().__init__()
        self.lv=s_lv
        self.w,self.h=69*3,18*2
        self.damage=s_lv*4+(main_state.player.my_skill[3]*2)
        self.frame=0
        self.framecount=0
        self.number=num
        self.y-=30-30*self.number
        if(self.number%2==0):
            self.x+=150
        else:
            self.x-=150

        if self.image==None:
            self.image=load_image("res/vfx/whip.png")

    def update(self):
        self.framecount+=1
        if(self.framecount==10):
            game_world.remove_object(self) 
        self.frame=self.framecount//2
    
    def draw(self):
        if(self.number%2==0):
            self.image.clip_composite_draw(69*self.frame, 0, 69, 18, 0, '', self.x, self.y, self.w, self.h)
        else:
            self.image.clip_composite_draw(69*self.frame, 0, 69, 18, 0, 'h', self.x, self.y, self.w, self.h)




