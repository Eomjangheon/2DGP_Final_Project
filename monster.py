from pico2d import*
import random
import main_state
import math
import game_world
import exp_jam
setXpos=[-1,0,1,-1,0,1,-1,0,1]
setYpos=[1,1,1,0,0,0,-1,-1,-1]
#모든 몬스터 종류의 부모 클래스
#몬스터별로 공통된 부분을 담고있다.
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
        self.dieFrame=0
        self.hp=0
        self.max_hp=0
        self.picMoveW,self.picMoveH,self.picDieW,self.picDieH=0,0,0,0
        self.isHitByWhipTimer=0

    def update(self):
        #캐릭터의 이동만큼 반대로 이동
        self.x-=main_state.player.dx ;  self.y-=main_state.player.dy
        #살아있는 상태라면
        if(self.isDie==False):
            #캐릭터를 향해 걷는 방향벡터를 구한다.    
            self.dx=640-self.x;             self.dy=400-self.y
            if self.dx==0:
                self.dx=0.00000001
            #속도의 정규화를 위해 각도를 구한다.
            self.theta=math.atan(self.dy/self.dx)
            if(self.dx<0):
                self.theta+=math.pi
            #삼각함수로 속도를 정규화한다.
            self.dx=math.cos(self.theta)*1
            self.dy=math.sin(self.theta)*1
            #사라지지 않는 채찍을 위한 타이머
            if(self.isHitByWhip):
                self.isHitByWhipTimer+=0.16
            if(self.isHitByWhipTimer>3):
                self.isHitByWhip=False
                self.isHitByWhipTimer=0
            self.x+=self.dx
            self.y+=self.dy
            #애니메이션의 자연스러움을 위한 연산
            self.frame_count=(self.frame_count+1)%32
            self.frame=self.frame_count//8
            self.hit()
            self.addforce()
        if(self.isDie==True):
            self.dieFrame+=1
            self.die()
            

    #죽자마자 경험치를 뱉고, 죽는 애니메이션 재생
    def die(self):
        if self.dieFrame==1:
            jam=exp_jam.Exp_jam(self.x,self.y,self.exp)
            game_world.add_object(jam,2)
        if self.dieFrame==30:
            game_world.remove_object(self)

    def draw(self):
        if self.isDie==False:
            #self.hp_bar.draw(self.x,self.y-20,30*(self.hp/self.max_hp),5)
            if(self.dx<0):
                self.move_image.clip_composite_draw(self.picMoveW*self.frame, 0, self.picMoveW, self.picMoveH, 0, '', self.x, self.y, self.w, self.h)
            else:
                self.move_image.clip_composite_draw(self.picMoveW*self.frame,0,self.picMoveW,self.picMoveH,0,'h',self.x,self.y,self.w,self.h)
        else:
            if(self.dx<0):
                self.die_image.clip_composite_draw(self.picDieW*self.dieFrame, 0, self.picDieW, self.picDieH, 0, '', self.x, self.y, self.w, self.h)
            else:
                self.die_image.clip_composite_draw(self.picDieW*self.dieFrame,0,self.picDieW,self.picDieH,0,'h',self.x,self.y,self.w,self.h)

    #몬스터끼리 겹치지 않게 서로 밀어낸다.
    #공간분할을 통해 프레임드랍을 줄였다.
    def addforce(self):
        teX=int((self.x+320)//80)
        teY=int((self.y+320)//80)
        for i in range(9):
            if teY+setYpos[i]>=0 and teY+setYpos[i]<18 and teX+setXpos[i]>=0 and teX+setXpos[i]<24:
                for mon in main_state.objectSpaceMon[teY+setYpos[i]][teX+setXpos[i]] :
                    if(mon!=self):
                        if(abs(mon.x-self.x)<(self.w) and abs(mon.y-self.y)<(self.h) and mon.isDie==False):
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
                            self.isDie=True
                            self.die()

#모든 몬스터 종류는 Monster를 상속받는다.
class Bat(Monster):
    move_image=None
    die_image=None
    def __init__(self):
        super().__init__()
        self.max_hp=10
        self.hp=10
        self.exp=1
        self.picMoveW=19
        self.picMoveH=21
        self.picDieW=55
        self.picDieH=36
        self.w=57
        self.h=63
        self.damage=3
        if self.move_image==None:
            self.move_image=load_image("res/monster/Bat1_move.png")
        if self.die_image==None:
            self.die_image=load_image("res/monster/Bat1_die.png")

class Armor(Monster):
    move_image=None
    die_image=None
    def __init__(self):
        super().__init__()
        self.max_hp=20
        self.hp=20
        self.exp=2
        self.picMoveW=38
        self.picMoveH=36
        self.picDieW=36
        self.picDieH=34
        self.w=76
        self.h=72
        self.damage=5
        if self.move_image==None:
            self.move_image=load_image("res/monster/Armor1_move.png")
        if self.die_image==None:
            self.die_image=load_image("res/monster/Armor1_die.png")

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

