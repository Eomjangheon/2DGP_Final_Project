from pico2d import*
from player import*
import main_state

class Main_state_ui:
    level_font=None

    def __init__(self):
        if self.level_font==None:
            self.level_font=load_font('res/fonts/KO.ttf',50)
    
    def draw(self):
        self.level_font.draw(340,70,"level: {} exp: {} expCoe:{}".format(main_state.player.level,main_state.player.exp,main_state.player.expCoe),(120,0,0))
        