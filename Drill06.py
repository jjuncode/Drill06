from shutil import move

from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('sprite.png')

mouse_x, mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_x,character_y = mouse_x,mouse_y
mouse_list = []
quit = False
hide_cursor()

class Ani:
    cur_frame =0
    offset_x = 74       # ani offset x
    offset_y = 80       # ani offset y 
    max_frame = [9,9,9,9,2,0,2,2]    # sprite max frame
    cur_ani = 0         # cur ani ( from img_bottom )

def Render():
    global mouse_x,mouse_y,character_x,character_y
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    DrawCursor()    # cursor
    MoveCharacter() # character move
    character.clip_draw(Ani.cur_frame*Ani.offset_x,Ani.cur_ani*Ani.offset_y,Ani.offset_x,Ani.offset_y
                        ,character_x,character_y)
    update_canvas()

def SetFrame():
    Ani.cur_frame += 1
    if (Ani.cur_frame > Ani.max_frame[Ani.cur_ani]):    # Frame reset
        Ani.cur_frame =0
def MoveCharacter():
    global character_x, character_y,mouse_x,mouse_y,move_speed
    if character_x < mouse_x :
        Ani.cur_ani = 0
    else :
        Ani.cur_ani = 2
    for i in range(0,100+1):
        SetFrame()  # animation
        t = i/100
        character_x = (1-t)*character_x + t*mouse_x
        character_y = (1-t)*character_y + t*mouse_y
def handle_event():
    global quit,mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit = True
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                quit=True
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
        elif ( event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT ):
            mouse_list.append((mouse_x,mouse_y))

def DrawCursor():
    global mouse_x, mouse_y, mouse_list
    mouse.draw(mouse_x,mouse_y)
    for pos in mouse_list:
        mouse.draw(pos[0],pos[1])

def main():
    while (not quit):
        handle_event()
        Render()

    close_canvas()


main()


