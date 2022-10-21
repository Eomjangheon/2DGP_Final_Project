import game_framework
import pico2d
import codeFile.stateCode.start_state as start_state

pico2d.open_canvas(1280,800)
game_framework.run(start_state)
pico2d.close_canvas()
