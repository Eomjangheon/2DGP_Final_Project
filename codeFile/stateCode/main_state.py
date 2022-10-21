from pico2d import *
from codeFile.classCode.background import*
import game_framework
import game_world
from codeFile.stateCode.main_state_ui import *
from codeFile.classCode.player import*
import codeFile.classCode.exp_jam as exp_jam
import codeFile.classCode.monster as monster
import codeFile.classCode.sound_manager as sound_manager
player=None
name = "mainState"
monTime=0
objectSpaceMon=[[[] for i in range (24)] for i in range(18)] 
objectSpaceSkill=[[[] for i in range (24)] for i in range(18)]
#현재는 스킬들의 텍스트를 여기서 관리하지만 나중에 파일입출력 예정
#index, name,
skill_name=[[0,'불의 지팡이','무작위 적을 향해 발사되며 큰 피해를 줍니다.','갯수가 1개 증가하고 크기가 커집니다.','갯수가 1개 증가하고 크기가 커집니다.','갯수가 1개 증가하고 크기가 커집니다.','갯수가 1개 증가하고 크기가 커집니다.'],
            [1,'채찍','수평으로 적을 관통해 공격합니다.','갯수가 1개 증가하고 강력해집니다.','갯수가 1개 증가하고 강력해집니다.','갯수가 1개 증가하고 강력해집니다.','갯수가 1개 증가하고 강력해집니다.'],
            [2,'마법의 오브','더 먼 거리의 아이템을 획득합니다.','더 먼 거리의 아이템을 획득합니다.','더 먼 거리의 아이템을 획득합니다.','더 먼 거리의 아이템을 획득합니다.','더 먼 거리의 아이템을 획득합니다.',],
            [3,'시금치','모든 공격의 데미지가 2증가합니다.','모든 공격의 데미지가 4증가합니다.','모든 공격의 데미지가 6증가합니다.','모든 공격의 데미지가 8증가합니다.','모든 공격의 데미지가 10증가합니다.',]
            ]
def enter():
    global bgm,sManager
    print("main")
    level_up_state.Level_up_state_ui.getSkill=[i for i in range(4)]
    mapSet=[[-1280,1280],[0,1280],[1280,1280],[-1280,0],[0,0],[1280,0],[-1280,-1280],[0,-1280],[1280,-1280]]
    global player,main_state_ui,backgrounds,objectSpaceMon,objectSpaceSkill
    objectSpaceMon=[[[] for i in range (24)] for i in range(18)] 
    objectSpaceSkill=[[[] for i in range (24)] for i in range(18)]
    player=None
    player=Player()
    sManager=[sound_manager.Sound_Manager() for i in range(100)]
    main_state_ui=Main_state_ui()
    backgrounds=[Background() for i in range(9)]
    for i in range(9):
            backgrounds[i].x+=mapSet[i][0]
            backgrounds[i].y+=mapSet[i][1]
    game_world.add_objects(backgrounds,0)
    game_world.add_object(player,1)
    game_world.add_object(main_state_ui,10)
    bgm=load_music('res/sound/ma.ogg')
    bgm.set_volume(value.volume)
    bgm.repeat_play()


def exit():
    global bgm
    #스테이트를 나갈때 게임월드를 초기화
    del(bgm)
    game_world.objects=[[],[],[],[],[],[],[],[],[],[],[]]



def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                player.dx=3
                player.prior_dir='Right'
            elif event.key==SDLK_LEFT:
                player.dx=-3
                player.prior_dir='Left'
            elif event.key==SDLK_UP:
                player.dy=3
            elif event.key==SDLK_DOWN:
                player.dy=-3
            elif event.key==SDLK_ESCAPE:
                mon=monster.Bat()
                game_world.add_object(mon,3)
        #방향키를 떼면 이전 방향을 기억하고, 뗀곳의 dx, dy조절
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                if(player.dx>0):
                    player.dx=0
            elif event.key==SDLK_LEFT:
                if(player.dx<0):
                    player.dx=0
            elif event.key==SDLK_UP:
                if(player.dy>0):
                    player.dy=0
            elif event.key==SDLK_DOWN:
                if(player.dy<0):
                    player.dy=0

def update():
    global player
    global monTime
    global objectSpaceMon
    global objectSpaceSkill
    monTime+=0.16
    #최대 몬스터 제한
    if(len(game_world.objects[3])<300 and monTime>1):
        mon=monster.Bat()
        game_world.add_object(mon,3)
        mon=monster.Armor()
        game_world.add_object(mon,3)
        monTime=0
    
    #공간분할 총 24*18칸
    objectSpaceMon=[[[] for k in range (24)] for i in range(18)] 
    objectSpaceSkill=[[[] for k in range (24)] for i in range(18)] 
    #몬스터 공간에 몬스터 삽입
    for mon in game_world.objects[3]:
        teY=int((mon.y+320)//80)
        teX=int((mon.x+320)//80)
        if(mon.x<1280+320 and mon.x>=-320 and mon.y<800+320 and mon.y>=-320):
            objectSpaceMon[teY][teX].append(mon)
    #스킬 공간에 스킬 삽입
    for skill in game_world.objects[4]:
        teY=int((skill.y+320)//80)
        teX=int((skill.x+320)//80)
        if(skill.x<1280+320 and skill.x>=-320 and skill.y<800+320 and skill.y>=-320):
            objectSpaceSkill[teY][teX].append(skill)        

    for game_object in game_world.all_objects():
        game_object.update()
    
    die()

#level_up_state를 위한 그리기 함수
def drawWorld():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    global player
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.016)

#캐릭터가 죽을경우 state변환
def die():
    global player
    if player.hp<=0:
        game_framework.change_state(start_state)
        

def pause(): pass
def resume(): pass
