from pico2d import*
import random
import codeFile.stateCode.main_state as main_state
import math
import game_world
import game_framework


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
        self.dx=math.cos(self.theta)
        self.dy=math.sin(self.theta)
        if FireBall.image==None:
            FireBall.image=load_image("res/vfx/fireball.png")
            
    def update(self):
        self.x-=main_state.player.dx*game_framework.frame_time*60
        self.y-=main_state.player.dy*game_framework.frame_time*60
        self.x+=self.dx*game_framework.frame_time*60*5
        self.y+=self.dy*game_framework.frame_time*60*5
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
        self.TIME_PER_ACTION=0.2
        self.ACTION_PER_TIME=1.0/self.TIME_PER_ACTION
        self.FRAMES_PER_ACTION = 5
        if(self.number%2==0):
            self.x+=150
        else:
            self.x-=150

        if Whip.image==None:
            Whip.image=load_image("res/vfx/whip.png")

    def update(self):
        self.frame = (self.frame + self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time)
        if(int(self.frame)==5):
            game_world.remove_object(self) 
    
    def draw(self):
        if(self.number%2==0):
            self.image.clip_composite_draw(69*int(self.frame), 0, 69, 18, 0, '', self.x, self.y, self.w, self.h)
        else:
            self.image.clip_composite_draw(69*int(self.frame), 0, 69, 18, 0, 'h', self.x, self.y, self.w, self.h)

class Axe(Skill):
    name='axe'
    image=None
    def __init__(self,s_lv,num):
        super().__init__()
        self.lv=s_lv
        self.w,self.h=18*(self.lv+1),20*(self.lv+1)
        self.damage=s_lv*4+(main_state.player.my_skill[4]*2)
        self.number=num
        self.rad=0
        self.dy=20
        self.ay=-1
        self.dx=-4+self.number*3
        self.speed=60

        if Axe.image==None:
            Axe.image=load_image("res/vfx/axe.png")

    def update(self):
        if(self.y<0):
            game_world.remove_object(self) 
        self.x-=main_state.player.dx*game_framework.frame_time*60
        self.y-=main_state.player.dy*game_framework.frame_time*60
        self.rad+=0.2*game_framework.frame_time*self.speed
        self.x+=self.dx*game_framework.frame_time*self.speed
        self.y+=self.dy*game_framework.frame_time*self.speed
        self.dy+=self.ay*game_framework.frame_time*self.speed
    
    def draw(self):
        self.image.composite_draw(self.rad, '', self.x, self.y, self.w, self.h)

class Book(Skill):
    name='book'
    image=None
    def __init__(self,s_lv,num):
        super().__init__()
        self.lv=s_lv
        self.w,self.h=12*(self.lv+1),16*(self.lv+1)
        self.damage=s_lv*4+(main_state.player.my_skill[5]*2)
        self.number=num
        self.rad=0
        self.timer=0
        self.speed=5

        if Book.image==None:
            Book.image=load_image("res/vfx/HolyBook.png")

    def update(self):
        if(self.timer>2.5):
            game_world.remove_object(self) 
        self.rad=self.rad+game_framework.frame_time*self.speed
        self.x=640+math.cos(self.rad+math.radians(360/self.lv*self.number))*40*self.lv
        self.y=400+math.sin(self.rad+math.radians(360/self.lv*self.number))*40*self.lv
        self.timer+=game_framework.frame_time
    
    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)



