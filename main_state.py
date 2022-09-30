from pico2d import *
from background import*
import game_framework
import title_state
from main_state_ui import *
from player import*
name = "mainState"
def enter():
    mapSet=[[-1280,1280],[0,1280],[1280,1280],[-1280,0],[0,0],[1280,0],[-1280,-1280],[0,-1280],[1280,-1280]]
    global player,main_state_ui,backgrounds
    player=Player()
    main_state_ui=Main_state_ui()
    backgrounds=[Background() for i in range(9)]
    for i in range(9):
        backgrounds[i].x+=mapSet[i][0]
        backgrounds[i].y+=mapSet[i][1]


def exit():
    global player,main_state_ui,backgrounds
    del(player)
    del(main_state_ui)
    del(backgrounds)


def handle_events(st):
    global player
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                player.dx=10
                player.prior_dir='Right'
            elif event.key==SDLK_LEFT:
                player.dx=-10
                player.prior_dir='Left'
            elif event.key==SDLK_UP:
                player.dy=10
            elif event.key==SDLK_DOWN:
                player.dy=-10
            elif event.key==SDLK_ESCAPE:
                pass
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
    global player,backgrounds
    player.update()
    for i in range(9):
        backgrounds[i].update()

def draw(st):
    global player, main_state_ui
    clear_canvas()
    for i in range(9):
        backgrounds[i].draw()
    player.draw()
    main_state_ui.draw()
    update_canvas()
    delay(0.02)

def pause(): pass
def resume(): pass

