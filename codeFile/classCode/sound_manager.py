from pico2d import*
import value
#main_state의 UI객체
class Sound_Manager:
    soundCheck=[False for i in range(4)]
    eatGemSound=None
    whip_sound=None
    monster_hit_sound=None
    axe_sound=None
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
    def gem_eat_sound(self):
        if not self.soundCheck[0]:
            self.eatGemSound.play()
            self.soundCheck[0]=True
    def Whip_sound(self):
        if not self.soundCheck[1]:
            self.whip_sound.play()
            self.soundCheck[1]=True
    def Axe_sound(self):
        if not self.soundCheck[2]:
            self.axe_sound.play()
            self.soundCheck[2]=True
    def Monster_hit_sound(self):
        if not self.soundCheck[3]:
            self.monster_hit_sound.play()
            self.soundCheck[3]=True
    def self_update(self):
        for i in range(4):
            self.soundCheck[i]=False


