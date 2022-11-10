from pico2d import*
import codeFile.stateCode.main_state as main_state
import game_framework

#배경 객체
#플레이어를 가운데 고정하므로 배경이 움직여야함
class Background:
    image = None
    def __init__(self):
        self.x,self.y=640,400
        if Background.image==None:
            Background.image=load_image('res/background/bg_forest.png')
    
    
    def update(self):
        #플레이어가 이동한 만큼 배경이 반대로 이동한다
        self.x-=main_state.player.dx*game_framework.frame_time*60
        self.y-=main_state.player.dy*game_framework.frame_time*60

        #무한맵을 만들기 위해 범위가 넘어가면 반대쪽에 다시 이동시킨다.
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

    


    

