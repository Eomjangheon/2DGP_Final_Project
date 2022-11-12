from pico2d import*
import value
#main_state의 UI객체
class Sound_Manager:
    soundCheck=[False for i in range(6)]
    eatGemSound=None
    whip_sound=None
    monster_hit_sound=None
    axe_sound=None
    lvup_sound=None
    book_sound=None
    sound_stack=0
    def __init__(self):
        if Sound_Manager.eatGemSound==None:
            Sound_Manager.eatGemSound=load_wav('res/sound/get_gem_sound.wav')
            Sound_Manager.eatGemSound.set_volume(value.volume)
        if Sound_Manager.whip_sound==None:
            Sound_Manager.whip_sound=load_wav('res/sound/skill_whip_sound.wav')
            Sound_Manager.whip_sound.set_volume(value.volume)
        if Sound_Manager.axe_sound==None:
            Sound_Manager.axe_sound=load_wav('res/sound/skill_whip_sound.wav')
            Sound_Manager.axe_sound.set_volume(value.volume)
        if Sound_Manager.monster_hit_sound==None:
            Sound_Manager.monster_hit_sound=load_wav('res/sound/enemy_hit_sound.wav')
            Sound_Manager.monster_hit_sound.set_volume(value.volume)
        if Sound_Manager.lvup_sound==None:
            Sound_Manager.lvup_sound=load_wav('res/sound/skill_whip_sound.wav')
            Sound_Manager.lvup_sound.set_volume(value.volume)
        if Sound_Manager.book_sound==None:
            Sound_Manager.book_sound=load_wav('res/sound/skill_whip_sound.wav')
            Sound_Manager.book_sound.set_volume(value.volume)
    def gem_eat_sound(self):
        if self.soundCheck[0]==False:
            self.eatGemSound.play()
            self.soundCheck[0]=True
    def Whip_sound(self):
        if self.soundCheck[1]==False:
            self.whip_sound.play()
            self.soundCheck[1]=True
    def Axe_sound(self):
        if self.soundCheck[2]==False:
            self.axe_sound.play()
            self.soundCheck[2]=True
    def Monster_hit_sound(self):
        if self.soundCheck[3]==False:
            self.monster_hit_sound.play()
            self.soundCheck[3]=True
    def Lvup_sound(self):
        if self.soundCheck[4]==False:
            self.lvup_sound.play()
            self.soundCheck[4]=True
    def Book_sound(self):
        if self.soundCheck[5]==False:
            self.book_sound.play()
            self.soundCheck[5]=True
    def self_update(self):
        self.sound_stack+=1
        self.sound_stack%=10
        if self.sound_stack==0:
            for i in range(6):
                self.soundCheck[i]=False


