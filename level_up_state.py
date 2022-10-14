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
#레벨업시 잠시 들어오는 state이다.
#여기서 스킬 레벨을 올릴수있다.
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
            #---------------------------------------
            #escape는 수정 예정이다. 지금은 개발자용 키
            #---------------------------------------
            if event.key==SDLK_ESCAPE:
                game_framework.pop_state()
            
            #스킬 선택 버튼이다. 스킬 개수에 맞게 이동가능하다.
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
    clear_canvas()
    global level_up_state_ui
    if(len(level_up_state_ui.getSkill)>0):
        main_state.main_state_ui.draw()
    else:
        game_framework.pop_state()
        return
    main_state.drawWorld()
    level_up_state_ui.draw()
    update_canvas()
    
    delay(0.02)

def pause(): pass
def resume(): pass

