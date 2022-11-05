from pico2d import*
from codeFile.classCode.player import*
import codeFile.stateCode.main_state as main_state
import value
#main_state의 UI객체
class Main_state_ui:
    level_font=None
    exp_box=None
    exp_bar=None
    
    def __init__(self):
        if Main_state_ui.level_font==None:
            Main_state_ui.level_font=load_font('res/fonts/KO.ttf',30)
        if Main_state_ui.exp_box==None:
            Main_state_ui.exp_box=load_image('res/ui/frameB9.png')
        if Main_state_ui.exp_bar==None:
            Main_state_ui.exp_bar=load_image('res/ui/exp_bar.png')
        
            
    def draw(self):
        self.exp_box.draw(640,780,1500,40)
        self.exp_bar.draw(main_state.player.exp/main_state.player.expCoe/2,782,main_state.player.exp/main_state.player.expCoe*2560,36)
        self.level_font.draw(1185,780,"LV: {}".format(main_state.player.level),(255,255,255))

    def update(self):
        pass