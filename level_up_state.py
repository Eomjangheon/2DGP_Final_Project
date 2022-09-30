from pico2d import *
import game_framework
import title_state
from main_state_ui import*
import main_state
from level_up_state_ui import*
name = "levelUpState"
def enter():
    global level_up_state_ui
    level_up_state_ui=Level_up_state_ui()
    pass

def exit():
    global level_up_state_ui
    del(level_up_state_ui)
    pass


def handle_events(st):
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                game_framework.pop_state()
                
        
def update(st):
    pass

def draw(st):
    global level_up_state_ui
    clear_canvas()
    main_state.player.draw()
    main_state.main_state_ui.draw()
    level_up_state_ui.draw()
    update_canvas()
    delay(0.02)


def pause(): pass
def resume(): pass

