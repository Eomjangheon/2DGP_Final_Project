from pico2d import*
import random
import codeFile.stateCode.main_state as main_state
import game_world
import value
import game_framework
import codeFile.classCode.sound_manager as sound_manager
#경험치 객체
#몬스터가 죽으면 생기는 경험치 보석
class Exp_jam:
    image=None
    #몬스터의 위치와 경험치를 인자로 받는다.
    def __init__(self,inX,inY,inExp):
        self.x,self.y=inX,inY
        self.dx,self.dy=0,0
        self.ax,self.ay=0,0
        self.count=0
        self.exp=inExp
        self.isEat=False
        if Exp_jam.image==None:
            Exp_jam.image=load_image("res/vfx/GemGreen.png")
        

    def update(self):
        #캐릭터가 움직이는 반대방향 이동
        self.x-=main_state.player.dx*game_framework.frame_time*60
        self.y-=main_state.player.dy*game_framework.frame_time*60

        #캐릭터의 아이템 흡수범위
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

    #플레이어가 먹었을때의 이동이다.
    #총 10프레임으로 가속도 a를 주어 잠시 멀어졌다가 빨려들어온다.
    #모든 보석은 10프레임에 맞춰 흡수
    def eat(self):
            
        self.x+=self.dx*game_framework.frame_time*60
        self.y+=self.dy*game_framework.frame_time*60
        self.dx+=self.ax*game_framework.frame_time*60
        self.dy+=self.ay*game_framework.frame_time*60
        self.count+=game_framework.frame_time
        if self.count>0.16:
            main_state.player.exp+=self.exp
            main_state.sManager[value.num].gem_eat_sound()
            game_world.remove_object(self)
    
    #정확히 10프레임으로 캐릭터에 가기 위한
    #속도와 가속도를 세팅한다.
    def eatSet(self):
            self.isEat=True
            self.dx=(self.x-640)/5
            self.ax=-self.dx/3
            self.dy=(self.y-400)/5
            self.ay=-self.dy/3



