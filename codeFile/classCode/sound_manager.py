from pico2d import*
import value
#main_state의 UI객체
class Sound_Manager:
    eatGemSound=None
    whip_sound=None
    monster_hit_sound=None
    def __init__(self):
        if Sound_Manager.eatGemSound==None:
            Sound_Manager.eatGemSound=load_wav('res/sound/get_gem_sound.wav')
            Sound_Manager.eatGemSound.set_volume(value.volume)
        if Sound_Manager.whip_sound==None:
            Sound_Manager.whip_sound=load_wav('res/sound/skill_whip_sound.wav')
            Sound_Manager.whip_sound.set_volume(value.volume)
        if Sound_Manager.monster_hit_sound==None:
            Sound_Manager.monster_hit_sound=load_wav('res/sound/enemy_hit_sound.wav')
            Sound_Manager.monster_hit_sound.set_volume(value.volume)
    def gem_eat_sound(self):
        self.eatGemSound.play()
        print(value.num)
    def Whip_sound(self):
        self.whip_sound.play()
        print(value.num)
    def Monster_hit_sound(self):
        self.monster_hit_sound.play()
        print(value.num)
    