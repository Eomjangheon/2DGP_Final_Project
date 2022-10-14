from os import remove
from pico2d import *
import game_framework
import title_state
import random
from main_state_ui import*
import main_state
from level_up_state_ui import*
import game_world
name = "levelUpState"
def enter():
    global level_up_state_ui
    level_up_state_ui=Level_up_state_ui()
    random.shuffle(level_up_state_ui.getSkill)
    print(main_state.player.my_skill)
    pass

def exit():
    global level_up_state_ui
    del(level_up_state_ui)
    pass


def handle_events():
    global level_up_state_ui
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key==SDLK_DOWN and level_up_state_ui.selectNum<len(level_up_state_ui.getSkill)-1:
                level_up_state_ui.selectNum+=1
            elif event.key==SDLK_UP and level_up_state_ui.selectNum>0:
                level_up_state_ui.selectNum-=1
            elif event.key==SDLK_SPACE:
                main_state.player.my_skill[level_up_state_ui.getSkill[level_up_state_ui.selectNum]]+=1
                if(main_state.player.my_skill[level_up_state_ui.getSkill[level_up_state_ui.selectNum]]==4):
                    level_up_state_ui.getSkill.remove(level_up_state_ui.getSkill[level_up_state_ui.selectNum])
                game_framework.pop_state()
        
def update():
    pass

def draw():
    global level_up_state_ui
    clear_canvas()
    if(len(level_up_state_ui.getSkill)>0):
        main_state.main_state_ui.draw()
    else:
        game_framework.pop_state()
        return
    for i in range(9):
        main_state.backgrounds[i].draw()
    main_state.player.draw()
    level_up_state_ui.draw()
    update_canvas()
    
    delay(0.02)


def pause(): pass
def resume(): pass

