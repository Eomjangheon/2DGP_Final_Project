from pico2d import*
import random
import main_state

class Exp_jam:
    image=None
    def __init__(self):
        self.x,self.y=random.randint(0,1280),random.randint(0,800)
        self.exp=2
        if self.image==None:
            self.image=load_image("res/vfx/GemGreen.png")

    def update(self):
        self.x-=main_state.player.dx
        self.y-=main_state.player.dy

    def draw(self):
        self.image.draw(self.x,self.y)


