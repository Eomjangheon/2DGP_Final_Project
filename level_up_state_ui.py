from pico2d import *
from player import*
import level_up_state
import main_state

class Level_up_state_ui:
    level_up_font=None
    description_font=None
    levelup_frame=None
    skill_frame=None

    def __init__(self):
        if self.level_up_font==None:
            self.level_up_font=load_font('res/fonts/KO.ttf',40)
        if self.description_font==None:
            self.description_font=load_font('res/fonts/KO.ttf',30)
        if self.levelup_frame==None:
            self.levelup_frame=load_image('res/ui/levelup_frame.png')
        if self.skill_frame==None:
            self.skill_frame=load_image('res/ui/frame_skill.png')
    
    def draw(self):
        self.levelup_frame.draw(640,380,600,650)
        self.level_up_font.draw(550,600,"Level Up!",(255,255,255))