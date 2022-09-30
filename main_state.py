from pico2d import *
import game_framework
import title_state
from player import*
def enter():
    global player
    player=Player()

def exit():
    global player
    del(player)


def handle_events(st):
    global player
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                player.dx+=1
            elif event.key==SDLK_LEFT:
                player.dx-=1
            elif event.key==SDLK_UP:
                player.dy+=1
            elif event.key==SDLK_DOWN:
                player.dy-=1
            elif event.key==SDLK_ESCAPE:
                pass
        #방향키를 떼면 이전 방향을 기억하고, 뗀곳의 dx, dy조절
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                player.dx-=1
                player.prior_dir='Right'
            elif event.key==SDLK_LEFT:
                player.dx+=1
                player.prior_dir='Left'
            elif event.key==SDLK_UP:
                player.dy-=1
            elif event.key==SDLK_DOWN:
                player.dy+=1


def update(st):
    global player
    player.update()

def draw(st):
    clear_canvas()
    player.draw()
    update_canvas()
    delay(0.02)

def pause(): pass
def resume(): pass

