from pico2d import*
import main_state

class Background:
    image = None
    def __init__(self):
        self.x,self.y=640,400
        if Background.image==None:
            Background.image=load_image('res/background/bg_forest.png')
    
    def update(self):
        self.x-=main_state.player.dx
        self.y-=main_state.player.dy
        if(self.x<-1920):
            self.x+=3840
        if(self.x>3200):
            self.x-=3840
        if(self.y<-2160):
            self.y+=3840
        if(self.y>2960):
            self.y-=3840
        
    
    def draw(self):
        self.image.draw(self.x,self.y,1280,1280)

    


    

