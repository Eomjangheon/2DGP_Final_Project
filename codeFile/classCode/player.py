from pico2d import*
import codeFile.stateCode.level_up_state as level_up_state
import game_framework
import codeFile.stateCode.main_state as main_state
import codeFile.classCode.skill as skill
import game_world
import codeFile.stateCode.start_state as start_state
import value

class Player:
    image = None
    hp_bar=None
    def __init__(self):
        self.x,self.y=640,400
        self.dx,self.dy=0,0
        self.prior_dir='Right'
        self.frame=0
        self.frame_count=0
        self.level=1
        self.exp=0
        self.hp=200
        self.max_hp=200
        self.expCoe=20
        self.hitTimer=0
        self.grabDis=50
        #fireball
        self.my_skill=[2,2,2,2,2,2,2,2]
        self.timerSkill=0
        self.timerSkill1=0
        self.timerSkill2=0
        self.timerSkill3=0
        self.skill1_counter=0
        self.skill2_counter=0
        self.TIME_PER_ACTION=0.5
        self.ACTION_PER_TIME=1.0/self.TIME_PER_ACTION
        self.FRAMES_PER_ACTION = 4
        
        if Player.image==None:
            Player.image=load_image('res/character/Antonio_Sheet.png')
        if Player.hp_bar==None:
            Player.hp_bar=load_image('res/ui/button_c8_normal.png')
    
    def update(self):
        self.hp-=1
        self.frame = (self.frame + self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time)%4


        self.timerSkill+=game_framework.frame_time
        self.timerSkill1+=game_framework.frame_time
        self.timerSkill2+=game_framework.frame_time
        self.timerSkill3+=game_framework.frame_time
        if self.exp>=self.expCoe:
            self.level_up()

        if self.my_skill[0]!=0:
            if self.timerSkill>0.5:
                self.fire_ball()
                self.timerSkill%=0.5

        if self.my_skill[1]!=0:
            if int(self.timerSkill1*4)==self.skill1_counter:
                self.whip(self.skill1_counter)
                self.skill1_counter=(self.skill1_counter+1)%self.my_skill[1]
                    
        if(self.timerSkill1>2):
            self.timerSkill1%=2

        
        if self.my_skill[4]!=0:
            if int(self.timerSkill2*4)==self.skill2_counter:
                self.axe(self.skill2_counter)
                self.skill2_counter=(self.skill2_counter+1)%self.my_skill[4]
                    
        if(self.timerSkill2>2):
            self.timerSkill2%=2

        if self.my_skill[5]!=0:
            if(self.timerSkill3<1):
                for i in range(self.my_skill[5]):
                    self.book(i)
                self.timerSkill3=2
            self.timerSkill3%=5
        
        self.hit()
    
    def draw(self):
        if(self.dx == 0 and self.dy == 0):
            if(self.prior_dir=='Right'):
                self.image.clip_draw(0,0,32,32,self.x,self.y,64,64)
            else:
                self.image.clip_composite_draw(0,0,32,32,0,'h',self.x,self.y,64,64)
        elif(self.dx>0):
            self.image.clip_draw(int(self.frame)*32,0,32,32,self.x,self.y,64,64)
        elif(self.dx<0):
            self.image.clip_composite_draw(int(self.frame)*32,0,32,32,0,'h',self.x,self.y,64,64)
        elif(self.dy!=0):
            if self.prior_dir=='Right':
                self.image.clip_draw(int(self.frame)*32,0,32,32,self.x,self.y,64,64)
            elif self.prior_dir=='Left':
                self.image.clip_composite_draw(int(self.frame)*32,0,32,32,0,'h',self.x,self.y,64,64)
        self.hp_bar.draw(640,350,100*(self.hp/self.max_hp),10)

    def level_up(self):
        self.level+=1
        self.exp-=self.expCoe
        self.expCoe*=1.1
        self.set_stop()
        
        main_state.draw()
        game_framework.push_state(level_up_state)

    def set_stop(self):
        if(self.dx>0):
            self.prior_dir='Right'
        else:
            self.prior_dir='Left'
        self.dx=0
        self.dy=0

    #몬스터에게 닿았을때
    def hit(self):
        if(self.hitTimer==0):
            for i in range(8,10+1):
                for j in range(11,13+1):
                    for mon in main_state.objectSpaceMon[i][j]:
                        if(abs(mon.x-640)<16+mon.w and abs(mon.y-400)<16+mon.h):
                            if mon.isDie==False:
                                self.hp-=mon.damage
                                self.hitTimer+=1
                                return
        else:
            self.hitTimer=(self.hitTimer+1)%10
            
                
    #화염구 스킬
    def fire_ball(self):
        for i in range(self.my_skill[0]):
            fireball=skill.FireBall(self.my_skill[0])
            game_world.add_object(fireball,4)
    #채찍스킬
    def whip(self,num):
        whip=skill.Whip(self.my_skill[1],num)
        game_world.add_object(whip,4)
        main_state.sManager[value.num].Whip_sound()

    def axe(self,num):
        axe_attack=skill.Axe(self.my_skill[4],num)
        game_world.add_object(axe_attack,4)
        main_state.sManager[value.num].Axe_sound()

    def book(self,num):
        book_attack=skill.Book(self.my_skill[5],num)
        game_world.add_object(book_attack,4)
        main_state.sManager[value.num].Axe_sound()