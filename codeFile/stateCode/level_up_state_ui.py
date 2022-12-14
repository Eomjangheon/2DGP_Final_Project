from pico2d import *
from codeFile.classCode.player import*
import codeFile.stateCode.level_up_state as level_up_state
import codeFile.stateCode.main_state as main_state
import codeFile.classCode.player as player
#레벨업 스테이트에서 ui를 담당하는 객체이다.
class Level_up_state_ui:
    level_up_font=None
    description_font=None
    description_font2=None
    levelup_frame=None
    skill_frame=None
    arrow=None
    item_frame=None
    #구현된 스킬, 패시브 개수만큼
    skill_img=[None for i in range(8)]
    getSkill=[i for i in range(8)]

    def __init__(self):
        if Level_up_state_ui.level_up_font==None:
            Level_up_state_ui.level_up_font=load_font('res/fonts/KO.ttf',40)
        if Level_up_state_ui.description_font==None:
            Level_up_state_ui.description_font=load_font('res/fonts/KO.ttf',30)
        if Level_up_state_ui.description_font2==None:
            Level_up_state_ui.description_font2=load_font('res/fonts/KO.ttf',20)
        if Level_up_state_ui.levelup_frame==None:
            Level_up_state_ui.levelup_frame=load_image('res/ui/levelup_frame.png')
        if Level_up_state_ui.skill_frame==None:
            Level_up_state_ui.skill_frame=load_image('res/ui/frame_skill.png')
        if Level_up_state_ui.arrow==None:
            Level_up_state_ui.arrow=load_image('res/ui/arrow.png')
        if Level_up_state_ui.item_frame==None:
            Level_up_state_ui.item_frame=load_image('res/ui/frameB9.png')
        if Level_up_state_ui.skill_img[0]==None:
            Level_up_state_ui.skill_img[0]=load_image('res/ui/WandBall.png')
        if Level_up_state_ui.skill_img[1]==None:
            Level_up_state_ui.skill_img[1]=load_image('res/ui/Whip.png')
        if Level_up_state_ui.skill_img[2]==None:
            Level_up_state_ui.skill_img[2]=load_image('res/ui/OrbGlow.png')
        if Level_up_state_ui.skill_img[3]==None:
            Level_up_state_ui.skill_img[3]=load_image('res/ui/Leaf.png')
        if Level_up_state_ui.skill_img[4]==None:
            Level_up_state_ui.skill_img[4]=load_image('res/ui/Axe.png')
        if Level_up_state_ui.skill_img[5]==None:
            Level_up_state_ui.skill_img[5]=load_image('res/ui/HolyBook.png')
        if Level_up_state_ui.skill_img[6]==None:
            Level_up_state_ui.skill_img[6]=load_image('res/ui/Wing.png')
        if Level_up_state_ui.skill_img[7]==None:
            Level_up_state_ui.skill_img[7]=load_image('res/ui/Ring.png')
        self.selectNum=0
        

    def update(self):
        pass
    
    def draw(self):
        #얻을 수 있는, 남은 스킬의 갯수다.
        #3개보다 적을 경우 빈 칸 선택 방지를 위해 num을 사용했다.
        if len(self.getSkill)<3:
            num=len(self.getSkill)
        else:
            num=3

        #ui의 전체적인 골격이다.
        self.levelup_frame.draw(640,380,600,650)
        self.level_up_font.draw(550,600,"Level Up!",(255,255,255))
        self.arrow.draw(330,500-self.selectNum*150,100,100)
        self.arrow.composite_draw(0,'h',950,500-self.selectNum*150,100,100)
        for i in range(3):
            self.skill_frame.draw(640,500-150*i,500,120)
            self.item_frame.draw(460,520-150*i,50,50)
        
        #선택가능한 스킬들을 골격위에 그린다.
        #정보는 main_state에서 받아오며 json으로 수정예정
        for i in range(num):
            self.skill_img[self.getSkill[i]].draw(460,520-150*i,40,40)
            self.description_font.draw(500,520-150*i,main_state.skill_name[self.getSkill[i]][1],(255,255,255))
            self.description_font2.draw(450,470-150*i,main_state.skill_name[self.getSkill[i]][2+main_state.player.my_skill[self.getSkill[i]]],(255,255,255))
            self.description_font2.draw(800,520-150*i,'lv: {}'.format(main_state.player.my_skill[self.getSkill[i]]+1),(255,255,255))
