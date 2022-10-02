from pico2d import*
from player import*
import main_state

class Main_state_ui:
    level_font=None
    exp_box=None
    exp_bar=None

    def __init__(self):
        if self.level_font==None:
            self.level_font=load_font('res/fonts/KO.ttf',30)
        if self.exp_box==None:
            self.exp_box=load_image('res/ui/frameB9.png')
        if self.exp_bar==None:
            self.exp_bar=load_image('res/ui/exp_bar.png')
    
    def draw(self):
        self.exp_box.draw(640,780,1500,40)
        self.exp_bar.draw(main_state.player.exp/main_state.player.expCoe/2,782,main_state.player.exp/main_state.player.expCoe*2560,36)
        self.level_font.draw(1185,780,"LV: {}".format(main_state.player.level),(255,255,255))

    def update(self):
        pass