from pico2d import*
import random
import main_state
import math
import game_world
import exp_jam

class Monster:
    def __init__(self):
        self.w,self.h=0,0
        self.rad=math.radians(random.randint(0,360))
        self.x=640+math.cos(self.rad)*640
        self.y=400+math.sin(self.rad)*400
        self.damage=0
        self.dx, self.dy, self.exp=0,0,0
        self.h, self.w=0,0
        self.isDie=False
        self.frame, self.frame_count=0,0

    def update(self):
        self.x-=main_state.player.dx ;  self.y-=main_state.player.dy
        self.dx=640-self.x;             self.dy=400-self.y
        if self.dx==0:
            self.dx=0.00000001
        self.theta=math.atan(self.dy/self.dx)
        if(self.dx<0):
            self.theta+=math.pi
        self.dx=math.cos(self.theta)*1
        self.dy=math.sin(self.theta)*1

        self.x+=self.dx
        self.y+=self.dy
        self.frame_count=(self.frame_count+1)%32
        self.frame=self.frame_count//8
        self.hit()
        #if(self.x>500 and self.x<800):
            #self.die()
    
    def die(self):
        jam=exp_jam.Exp_jam(self.x,self.y,self.exp)
        game_world.add_object(jam,self.exp)
        game_world.remove_object(self)

    def draw(self):
        if(self.dx<0):
            self.move_image.clip_composite_draw(self.w*self.frame, 0, self.w, self.h, 0, '', self.x, self.y, self.w*2, self.h*2)
        else:
            self.move_image.clip_composite_draw(self.w*self.frame,0,self.w,self.h,0,'h',self.x,self.y,self.w*2,self.h*2)

    def hit(self):
        for skill in game_world.objects[4]:
            if(abs(skill.x-self.x)<(skill.w+self.w)/2 and abs(skill.y-self.y)<(skill.h+self.h)/2):
                game_world.remove_object(skill)
                self.die()

class Bat(Monster):
    move_image=None
    die_image=None
    def __init__(self):
        super().__init__()
        self.exp=1
        self.w=19
        self.h=21
        if self.move_image==None:
            self.move_image=load_image("res/monster/Bat1_move.png")
        if self.die_image==None:
            self.die_image=load_image("res/monster/Bat1_die.png")



