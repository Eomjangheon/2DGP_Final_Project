from pico2d import *
from player import*
import level_up_state
import main_state
import player

class Level_up_state_ui:
    level_up_font=None
    description_font=None
    description_font2=None
    levelup_frame=None
    skill_frame=None
    arrow=None
    item_frame=None
    skill_img=[None for i in range(3)]
    getSkill=[i for i in range(3)]

    def __init__(self):
        if self.level_up_font==None:
            self.level_up_font=load_font('res/fonts/KO.ttf',40)
        if self.description_font==None:
            self.description_font=load_font('res/fonts/KO.ttf',30)
        if self.description_font2==None:
            self.description_font2=load_font('res/fonts/KO.ttf',20)
        if self.levelup_frame==None:
            self.levelup_frame=load_image('res/ui/levelup_frame.png')
        if self.skill_frame==None:
            self.skill_frame=load_image('res/ui/frame_skill.png')
        if self.arrow==None:
            self.arrow=load_image('res/ui/arrow.png')
        if self.item_frame==None:
            self.item_frame=load_image('res/ui/frameB9.png')
        if self.skill_img[0]==None:
            self.skill_img[0]=load_image('res/ui/WandBall.png')
        if self.skill_img[1]==None:
            self.skill_img[1]=load_image('res/ui/Whip.png')
        if self.skill_img[2]==None:
            self.skill_img[2]=load_image('res/ui/OrbGlow.png')
        self.selectNum=0
        

    def update(self):
        pass
    
    def draw(self):
        self.levelup_frame.draw(640,380,600,650)
        self.level_up_font.draw(550,600,"Level Up!",(255,255,255))
        self.arrow.draw(330,500-self.selectNum*150,100,100)
        self.arrow.composite_draw(0,'h',950,500-self.selectNum*150,100,100)
        for i in range(3):
            self.skill_frame.draw(640,500-150*i,500,120)
            self.item_frame.draw(460,520-150*i,50,50)

        for i in range((len(self.getSkill))%4):
            self.skill_img[self.getSkill[i]].draw(460,520-150*i,40,40)
            self.description_font.draw(500,520-150*i,main_state.skill_name[self.getSkill[i]][1],(255,255,255))
            self.description_font2.draw(450,470-150*i,main_state.skill_name[self.getSkill[i]][2+main_state.player.my_skill[self.getSkill[i]]],(255,255,255))
            self.description_font2.draw(800,520-150*i,'lv: {}'.format(main_state.player.my_skill[self.getSkill[i]]+1),(255,255,255))
