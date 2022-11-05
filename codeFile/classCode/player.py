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
        self.my_skill=[2,2,1,2]
        self.timerSkill=0
        self.timerSkill1=0
        
        if Player.image==None:
            Player.image=load_image('res/character/Antonio_Sheet.png')
        if Player.hp_bar==None:
            Player.hp_bar=load_image('res/ui/button_c8_normal.png')
    
    def update(self):
        self.frame_count=(self.frame_count+1)%32
        self.frame=self.frame_count//8
        #self.exp+=1
        #self.hp-=1

        self.timerSkill+=0.16
        self.timerSkill1+=0.16
        if self.exp>=self.expCoe:
            self.level_up()
        if self.my_skill[0]!=0:
            if self.timerSkill>2:
                self.fire_ball()
                self.timerSkill=0

        if self.my_skill[1]!=0:
            for i in range(self.my_skill[1]):
                if abs(self.timerSkill1-0.8*(i+1))<0.1:
                    self.whip(i)
                    
        if(self.timerSkill1>5):
            self.timerSkill1=0
        self.hit()
    
    def draw(self):
        if(self.dx == 0 and self.dy == 0):
            if(self.prior_dir=='Right'):
                self.image.clip_draw(0,0,32,32,self.x,self.y,64,64)
            else:
                self.image.clip_composite_draw(0,0,32,32,0,'h',self.x,self.y,64,64)
        elif(self.dx>0):
            self.image.clip_draw(self.frame*32,0,32,32,self.x,self.y,64,64)
        elif(self.dx<0):
            self.image.clip_composite_draw(self.frame*32,0,32,32,0,'h',self.x,self.y,64,64)
        elif(self.dy!=0):
            if self.prior_dir=='Right':
                self.image.clip_draw(self.frame*32,0,32,32,self.x,self.y,64,64)
            elif self.prior_dir=='Left':
                self.image.clip_composite_draw(self.frame*32,0,32,32,0,'h',self.x,self.y,64,64)
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

    