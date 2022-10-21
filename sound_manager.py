from pico2d import*
from player import*
import main_state
import value
#main_state의 UI객체
class Sound_Manager:
    eatGemSound=None
    whip_sound=None
    def __init__(self):
        if self.eatGemSound==None:
            self.eatGemSound=load_wav('res/sound/get_gem_sound.wav')
            self.eatGemSound.set_volume(value.volume)
        if self.whip_sound==None:
            self.whip_sound=load_wav('res/sound/skill_whip_sound.wav')
            self.whip_sound.set_volume(value.volume)
    def gem_eat_sound(self):
        self.eatGemSound.play()
    def Whip_sound(self):
        self.whip_sound.play()
    