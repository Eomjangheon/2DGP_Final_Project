from pico2d import *
import game_framework
import title_state
import main_state
name = "StartState"
image = []

start_font=None
font_time=0.0

def enter():
    global image, start_font
    image.append(load_image('res/start_img/introBG.png'))
    image.append(load_image('res/start_img/antonio.png'))
    image.append(load_image('res/start_img/imelda.png'))
    image.append(load_image('res/start_img/villain.png'))
    image.append(load_image('res/start_img/title.png'))
    start_font=load_font('res/fonts/KO.ttf',50)
def exit():
    global image,start_font
    del(image)
    del(start_font)

def update(a):
    global font_time
    delay(0.01)
    font_time = (font_time+0.01)%2


def draw(a):
    global image,start_font,font_time
    clear_canvas()
    image[0].draw(640, 400,1280,800)
    image[2].composite_draw(0,'h',1100, 400,600,600)
    image[3].draw(200, 200,700,1000)
    image[1].draw(640, 200,800,400)
    image[4].draw(640, 600,400,200)
    if(font_time<1.5):
        start_font.draw(340,70,"press Space Bar to start",(255,255,255))
    update_canvas()

def handle_events(a):
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_SPACE:
            game_framework.change_state(main_state)