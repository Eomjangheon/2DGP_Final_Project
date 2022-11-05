from os import remove
from pico2d import *
import game_framework
from codeFile.stateCode.main_state_ui import*
import codeFile.stateCode.main_state as main_state
from codeFile.stateCode.level_up_state_ui import*


name = "pause_state"
image=None
#레벨업시 잠시 들어오는 state이다.
#여기서 스킬 레벨을 올릴수있다.
def enter():
    global image
    image=load_image('res/ui/pause.png')

def exit():
    global image
    del image
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            #---------------------------------------
            #escape는 수정 예정이다. 지금은 개발자용 키
            #---------------------------------------
            if event.key==SDLK_ESCAPE:
                game_framework.pop_state()

        
def update():
    pass

def draw():
    global image
    clear_canvas()
    main_state.drawWorld()
    image.draw(640,400,300,300)
    update_canvas()
    
    delay(0.02)

def pause(): pass
def resume(): pass

