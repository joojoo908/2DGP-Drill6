from pico2d import *
import math
import random

move=1;
key = False;
x=300
y=400
up,down,r,l = 0,0,0,0

TUK_WIDTH, TUK_HEIGHT = 1280 , 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

handx=random.randrange(1,TUK_WIDTH)
handy=random.randrange(1,TUK_HEIGHT)

back = load_image('TUK_GROUND_FULL.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def len(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def move_all(frame,move,x,y, rad):
    rad=rad/180* math.pi
    clear_canvas()
    back.draw(TUK_WIDTH/2, TUK_HEIGHT/2)
    character.clip_composite_draw(frame*100, move*100 ,100,100 ,rad,'i',x,y,100,100)
    #character.clip_composite_draw(frame*100,0,100,100 ,rad,'v',x,y,100,100)
    update_canvas()
    delay(0.1)
    
def run(x1,y1,x2,y2):
    frame=0
    speed =10
    #(y2-y1)/(x2-x1)*x + y1 -x1*(y2-y1)/(x2-x1)
    for x in range(x1,x2,10):
        y = (y2-y1)/(x2-x1)*x + y1 -x1*(y2-y1)/(x2-x1)
        move_all(frame,1,x,y,0)
        frame = (frame+1)%8

def stand(x,y):
    print()

def handle_events():
    global move
    global key
    global up, down , r ,l
    global x,y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            move=5
        elif event.type == SDL_KEYDOWN:
            key =True
            if event.key==SDLK_RIGHT:
                r=1;
            if event.key==SDLK_LEFT:
                l=1
            if event.key==SDLK_UP:
                up=1
            if event.key==SDLK_DOWN:
                down =1
            if event.key==SDLK_ESCAPE:
                move=5
        elif event.type == SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                r=0
            if event.key==SDLK_LEFT:
                l=0
            if event.key==SDLK_UP:
                up=0
            if event.key==SDLK_DOWN:
                down =0
            if up==0 and down==0 and r==0 and l==0:
                key=0;
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x , TUK_HEIGHT-1 -event.y
        

frame=0
while 1:
    #run(0,0,500,500)
    #move=5
    handle_events()
    if move==5:
        break
    else:
        clear_canvas()
        back.draw(TUK_WIDTH/2, TUK_HEIGHT/2)
        hand.clip_composite_draw(0, 0 ,100,100 ,0,'i',x,y,50,50)
        update_canvas()
        #delay(0.001)
       
    #print(move)

    
close_canvas()
