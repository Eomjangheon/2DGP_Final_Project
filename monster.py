from pico2d import*
import random
import main_state
import math
import game_world
import exp_jam
setXpos=[-1,0,1,-1,0,1,-1,0,1]
setYpos=[1,1,1,0,0,0,-1,-1,-1]
class Monster:
    hp_bar=None
    def __init__(self):
        if Monster.hp_bar==None:
            Monster.hp_bar=load_image('res/ui/button_c8_normal.png')
        self.w,self.h=0,0
        self.rad=math.radians(random.randint(0,360))
        self.x=640+math.cos(self.rad)*800
        self.y=400+math.sin(self.rad)*600
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
        teX=int((self.x+320)//80)
        teY=int((self.y+320)//80)
        for i in range(9):
            if teY+setYpos[i]>=0 and teY+setYpos[i]<18 and teX+setXpos[i]>=0 and teX+setXpos[i]<24:
                for mon in main_state.objectSpaceMon[teY+setYpos[i]][teX+setXpos[i]] :
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
        teX=int((self.x+320)//80)
        teY=int((self.y+320)//80)
        for i in range(9):
            if teY+setYpos[i]>=0 and teY+setYpos[i]<18 and teX+setXpos[i]>=0 and teX+setXpos[i]<24:
                for skill in main_state.objectSpaceSkill[teY+setYpos[i]][teX+setXpos[i]] :
                    if(abs(skill.x-self.x)<(skill.w+self.w)/2 and abs(skill.y-self.y)<(skill.h+self.h)/2):
                        if(skill.name=='whip'):
                            if self.isHitByWhip==False:
                                if(self.x<=640):
                                    self.x-=30
                                else:
                                    self.x+=30
                                self.hp-=skill.damage
                                self.isHitByWhip=True
                                damage_font=DamageFont(self.x,self.y,skill.damage)
                                game_world.add_object(damage_font,5)
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
                            damage_font=DamageFont(self.x,self.y,skill.damage)
                            game_world.add_object(damage_font,5)
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
        self.exp=0
        self.w=57
        self.h=63
        if self.move_image==None:
            self.move_image=load_image("res/monster/Bat1_move.png")
        if self.die_image==None:
            self.die_image=load_image("res/monster/Bat1_die.png")

class DamageFont():
    damage_font=None
    png_info=[[0,170],[64,170],[128,170],[192,170],[0,85],[64,85],[128,85],[192,85],[0,0],[64,0]]
    def __init__(self,inX,inY,damage):
        if self.damage_font==None:
            self.damage_font=load_image("res/fonts/damage.png")
        self.fontX=inX
        self.fontY=inY
        self.timer=0
        self.size=30
        self.first=damage%10
        self.second=damage//10
    
    def update(self):
        self.fontX-=main_state.player.dx
        self.fontY-=main_state.player.dy
        self.timer+=0.16
        self.fontY+=1
        self.size-=1
        
        if(self.timer>3):
            game_world.remove_object(self)

    def draw(self):
        if(self.second==0):
            self.damage_font.clip_draw(self.png_info[self.first][0],self.png_info[self.first][1],64,85,self.fontX,self.fontY,self.size,self.size)
        else:
            self.damage_font.clip_draw(self.png_info[self.second][0],self.png_info[self.second][1],64,85,self.fontX-8,self.fontY,self.size,self.size)
            self.damage_font.clip_draw(self.png_info[self.first][0],self.png_info[self.first][1],64,85,self.fontX+8,self.fontY,self.size,self.size)

