from pico2d import*
import level_up_state
import game_framework
import main_state

class Player:
    image = None
    def __init__(self):
        self.x,self.y=640,400
        self.dx,self.dy=0,0
        self.prior_dir='Right'
        self.frame=0
        self.frame_count=0
        self.level=1
        self.exp=0
        self.expCoe=10
        if Player.image==None:
            Player.image=load_image('res/character/Antonio_Sheet.png')
    
    def update(self):
        self.frame_count=(self.frame_count+1)%32
        self.frame=self.frame_count//8
        self.x+=self.dx
        self.y+=self.dy
        self.exp+=1
        if self.exp>=self.expCoe:
            self.level_up()
    
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

    def level_up(self):
        self.level+=1
        self.exp-=self.expCoe
        self.expCoe*=1.1
        if(self.dx>0):
            self.prior_dir='Right'
        else:
            self.prior_dir='Left'
        self.dx=0
        self.dy=0
        
        main_state.draw(1)
        game_framework.push_state(level_up_state)


    

