from pico2d import*
from codeFile.classCode.player import*
import codeFile.stateCode.main_state as main_state
import value
import time
import game_framework
from codeFile.classCode.monster import*

#main_state의 UI객체
class Main_state_ui:
    level_font=None
    time_font=None
    exp_box=None
    exp_bar=None
    total_time=None
    total_second=40
    total_miniute=0
    is_spawn_hoodie=False
    mon_time=0
    level=0
    
    def __init__(self):
        if Main_state_ui.level_font==None:
            Main_state_ui.level_font=load_font('res/fonts/KO.ttf',30)
        if Main_state_ui.time_font==None:
            Main_state_ui.time_font=load_font('res/fonts/KO.ttf',40)
        if Main_state_ui.exp_box==None:
            Main_state_ui.exp_box=load_image('res/ui/frameB9.png')
        if Main_state_ui.exp_bar==None:
            Main_state_ui.exp_bar=load_image('res/ui/exp_bar.png')
        Main_state_ui.total_time=0
        
            
    def draw(self):
        self.exp_box.draw(640,780,1500,40)
        self.exp_bar.draw(main_state.player.exp/main_state.player.expCoe/2,782,main_state.player.exp/main_state.player.expCoe*2560,36)
        self.level_font.draw(1185,780,"LV: {}".format(main_state.player.level),(255,255,255))
        self.time_font.draw(600,720,"{} : {}".format(int(self.total_miniute),int(self.total_second)),(255,255,255))

    def update(self):
        self.mon_time+=game_framework.frame_time*(self.total_miniute+1)
        self.total_time+=game_framework.frame_time
        self.total_second=self.total_time%60
        self.total_miniute=self.total_time//60
        self.level=self.total_time//20
        if(int(self.total_time)==180 and self.is_spawn_hoodie==False):
            Main_state_ui.is_spawn_hoodie=True
            self.spawn_hoodie()
        if(len(game_world.objects[3])<300 and self.mon_time>0.5 and self.is_spawn_hoodie==False):
            if(self.level>=0 and self.level<5):
                mon=Bat()
                game_world.add_object(mon,3)
            if(self.level>=2 and self.level<7):
                mon=Armor()
                game_world.add_object(mon,3)
            if(self.level>=5):
                mon=Armor()
                game_world.add_object(mon,3)
            if(self.level>=4 and self.level<10):    
                mon=Buer()
                game_world.add_object(mon,3)
            if(self.level>=6):    
                mon=Buer()
                game_world.add_object(mon,3)
            self.mon_time=0
    def spawn_hoodie(self):
        for mon in game_world.objects[3]:
            mon.isDie=True
            mon.die()
        mon=Hoodie()
        game_world.add_object(mon,3)