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
    #구현된 스킬, 패시브 개수만큼
    

    def __init__(self):
        if Game_over_state_ui.game_over_font==None:
            Game_over_state_ui.game_over_font=load_font('res/fonts/KO.ttf',40)
            #여기부터
            
        # if Game_over_state_ui.quit_frame==None:
        #     Game_over_state_ui.quit_frame=load_image('res/ui/levelup_frame.png')
        # if Game_over_state_ui.skill_frame==None:
        #     Game_over_state_ui.skill_frame=load_image('res/ui/frame_skill.png')
        # if Game_over_state_ui.arrow==None:
        #     Game_over_state_ui.arrow=load_image('res/ui/arrow.png')
        # if Game_over_state_ui.item_frame==None:
        #     Game_over_state_ui.item_frame=load_image('res/ui/frameB9.png')

        

    def update(self):
        pass
    
    def draw(self):
        #self.levelup_frame.draw(640,380,600,650)
        self.game_over_font.draw(550,600,"Quit",(255,255,255))
        #self.arrow.draw(330,500-self.selectNum*150,100,100)
        #self.arrow.composite_draw(0,'h',950,500-self.selectNum*150,100,100)

