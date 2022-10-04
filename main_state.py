from pico2d import *
from background import*
import game_framework
import game_world
from main_state_ui import *
from player import*
import exp_jam
import monster
name = "mainState"
monTime=0
#index, name,
skill_name=[[0,'불의 지팡이','무작위 적을 향해 발사되며 큰 피해를 줍니다.','갯수가 1개 증가하고 강력해집니다.','크기가 커지며...','크기가 커지며...','크기가 커지며...'],
            [1,'채찍','수평으로 적을 관통해 공격합니다.','갯수가 1개 증가하고 강력해집니다.','갯수가 1개 증가하고 강력해집니다.','갯수가 1개 증가하고 강력해집니다.','갯수가 1개 증가하고 강력해집니다.']]
def enter():
    mapSet=[[-1280,1280],[0,1280],[1280,1280],[-1280,0],[0,0],[1280,0],[-1280,-1280],[0,-1280],[1280,-1280]]
    global player,main_state_ui,backgrounds,gems
    player=Player()
    main_state_ui=Main_state_ui()
    backgrounds=[Background() for i in range(9)]
    for i in range(9):
            backgrounds[i].x+=mapSet[i][0]
            backgrounds[i].y+=mapSet[i][1]
    game_world.add_objects(backgrounds,0)
    game_world.add_object(player,1)
    game_world.add_object(main_state_ui,10)
    


def exit():
    game_world.clear()


def handle_events(st):
    global player
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                player.dx=2
                player.prior_dir='Right'
            elif event.key==SDLK_LEFT:
                player.dx=-2
                player.prior_dir='Left'
            elif event.key==SDLK_UP:
                player.dy=2
            elif event.key==SDLK_DOWN:
                player.dy=-2
            elif event.key==SDLK_ESCAPE:
                mon=monster.Bat()
                game_world.add_object(mon,3)
        #방향키를 떼면 이전 방향을 기억하고, 뗀곳의 dx, dy조절
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                player.dx=0
            elif event.key==SDLK_LEFT:
                player.dx=0
            elif event.key==SDLK_UP:
                player.dy=0
            elif event.key==SDLK_DOWN:
                player.dy=0

def update(st):
    global monTime
    monTime+=0.16
    if(len(game_world.objects[3])<100):
        mon=monster.Bat()
        game_world.add_object(mon,3)
    
    for game_object in game_world.all_objects():
        game_object.update()

def draw(st):
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.016)

def pause(): pass
def resume(): pass

