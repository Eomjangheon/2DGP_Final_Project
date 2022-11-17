from os import remove
from pico2d import *
import game_framework
import title_state
import random
from codeFile.stateCode.main_state_ui import*
import codeFile.stateCode.main_state as main_state
import codeFile.stateCode.game_over_state_ui as game_over_state_ui
from codeFile.stateCode.level_up_state_ui import*
import game_world
import value
name = "gameOverState"
#게임오버시 들어오는 state이다.

def enter():
    global gou
    gou=game_over_state_ui.Game_over_state_ui()
    
    # bgm=load_wav('res/sound/level_up_sound.wav')
    # bgm.set_volume(value.volume)
    # bgm.play()
    

def exit():
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
                game_framework.quit()
            
            #스킬 선택 버튼이다. 스킬 개수에 맞게 이동가능하다.
            elif event.key==SDLK_SPACE:
                game_framework.change_state(start_state)
        
def update():
    pass

def draw():
    clear_canvas()
    global gou
    main_state.drawWorld()
    gou.draw()
    update_canvas()


def pause(): pass
def resume(): pass

