from pico2d import *
from codeFile.classCode.player import*
import codeFile.stateCode.level_up_state as level_up_state
import codeFile.stateCode.main_state as main_state
import codeFile.classCode.player as player
#레벨업 스테이트에서 ui를 담당하는 객체이다.
class Game_over_state_ui:
    game_over_font=None
    quit_frame=None
    game_over_image=None
    arrow=None
    gama_over_back=None
    #구현된 스킬, 패시브 개수만큼
    

    def __init__(self):
        if Game_over_state_ui.game_over_font==None:
            Game_over_state_ui.game_over_font=load_font('res/fonts/KO.ttf',40)
            
        if Game_over_state_ui.quit_frame==None:
            Game_over_state_ui.quit_frame=load_image('res/ui/button_c8_normal.png')
        if Game_over_state_ui.arrow==None:
            Game_over_state_ui.arrow=load_image('res/ui/arrow.png')
        if Game_over_state_ui.game_over_image==None:
            Game_over_state_ui.game_over_image=load_image('res/ui/gameOver.png')



        

    def update(self):
        pass
    
    def draw(self):
        self.quit_frame.draw(640,200,300,100)
        self.game_over_font.draw(600,200,"Quit",(255,255,255))
        self.arrow.draw(430,200,100,100)
        self.arrow.composite_draw(0,'h',850,200,100,100)
        self.game_over_image.draw(640,500,700,230)

