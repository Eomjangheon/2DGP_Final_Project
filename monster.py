from pico2d import*
import random
import main_state
import math
import game_world
import exp_jam

class Monster:
    hp_bar=None
    def __init__(self):
        if Monster.hp_bar==None:
            Monster.hp_bar=load_image('res/ui/button_c8_normal.png')
        self.w,self.h=0,0
        self.rad=math.radians(random.randint(0,360))
        self.x=640+math.cos(self.rad)*640
        self.y=400+math.sin(self.rad)*400
        self.damage=0
        self.dx, self.dy, self.exp=0,0,0
        self.h, self.w=0,0
        self.isDie=False
        self.isHitByWhip=False
        self.frame, self.frame_count=0,0
        self.hp=0
        self.max_hp=0
        self.isHitByWhipTimer=0

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
        if(self.isHitByWhip):
            self.isHitByWhipTimer+=0.16
        if(self.isHitByWhipTimer>3):
            self.isHitByWhip=False
            self.isHitByWhipTimer=0
        self.x+=self.dx
        self.y+=self.dy
        self.frame_count=(self.frame_count+1)%32
        self.frame=self.frame_count//8
        self.hit()
        self.addforce()
        #if(self.x>500 and self.x<800):
            #self.die()
    
    def die(self):
        jam=exp_jam.Exp_jam(self.x,self.y,self.exp)
        game_world.add_object(jam,2)
        game_world.remove_object(self)

    def draw(self):
        self.hp_bar.draw(self.x,self.y-20,30*(self.hp/self.max_hp),5)
        if(self.dx<0):
            self.move_image.clip_composite_draw(19*self.frame, 0, 19, 21, 0, '', self.x, self.y, self.w, self.h)
        else:
            self.move_image.clip_composite_draw(19*self.frame,0,19,21,0,'h',self.x,self.y,self.w,self.h)

    def addforce(self):
        for mon in game_world.objects[3]:
            if(mon!=self):
                if(abs(mon.x-self.x)<(self.w) and abs(mon.y-self.y)<(self.h)):
                    if(self.x>mon.x):
                        self.x+=1
                    else:
                        self.x-=1

                    if(self.y>mon.y):
                        self.y+=1
                    else:
                        self.y-=1

    def hit(self):
        for skill in game_world.objects[4]:
            if(abs(skill.x-self.x)<(skill.w+self.w)/2 and abs(skill.y-self.y)<(skill.h+self.h)/2):
                if(skill.name=='whip'):
                    if self.isHitByWhip==False:
                        if(self.x<=640):
                            self.x-=30
                        else:
                            self.x+=30
                        self.hp-=skill.damage
                        self.isHitByWhip=True
                        #damage_font=DamageFont(self.x,self.y,skill.damage)
                        #game_world.add_object(damage_font,5)
                else:
                    tempX=skill.x-self.x
                    tempY=skill.y-self.y
                    if tempX==0:
                        tempX=0.00000001
                    temptheta=math.atan(tempX/tempY)
                    if(tempX<0):
                        temptheta+=math.pi
                    self.x-=math.cos(self.theta)*20
                    self.y-=math.sin(self.theta)*20
                    self.hp-=skill.damage
                    #damage_font=DamageFont(self.x,self.y,skill.damage)
                    #game_world.add_object(damage_font,5)
                    game_world.remove_object(skill)
                if(self.hp<=0):
                    self.die()

class Bat(Monster):
    move_image=None
    die_image=None
    def __init__(self):
        super().__init__()
        self.max_hp=50
        self.hp=50
        self.exp=1
        self.w=57
        self.h=63
        if self.move_image==None:
            self.move_image=load_image("res/monster/Bat1_move.png")
        if self.die_image==None:
            self.die_image=load_image("res/monster/Bat1_die.png")

class DamageFont():
    damage_font=None
    def __init__(self,inX,inY,damage):
        if self.damage_font==None:
            self.damage_font=load_font('res/fonts/KO.ttf',15)
        self.fontX=inX
        self.fontY=inY
        self.timer=0
        self.string=str(damage)
    
    def update(self):
        self.fontX-=main_state.player.dx
        self.fontY-=main_state.player.dy
        self.timer+=0.16
        self.fontY+=1
        
        if(self.timer>3):
            game_world.remove_object(self)

    def draw(self):
        self.damage_font.draw(self.fontX,self.fontY+15,self.string,(255,255,255))


