from pico2d import*
from codeFile.classCode.player import*
import codeFile.stateCode.main_state as main_state
import value
import time
import game_framework

#main_state의 UI객체
class Main_state_ui:
    level_font=None
    time_font=None
    exp_box=None
    exp_bar=None
    total_time=None
    total_second=0
    total_miniute=0
    
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
        self.total_time+=game_framework.frame_time
        self.total_second=self.total_time%60
        self.total_miniute=self.total_time//60