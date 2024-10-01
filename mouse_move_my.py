from pico2d import *
import math
import random

key = False;

TUK_WIDTH, TUK_HEIGHT = 1280 , 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

handx=random.randrange(1,TUK_WIDTH)
handy=random.randrange(1,TUK_HEIGHT)

x=random.randrange(1,TUK_WIDTH)
y=random.randrange(1,TUK_HEIGHT)


back = load_image('TUK_GROUND_FULL.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def len(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def draw_all(frame,move,x,y, rad):
    global handx
    global handy
    
    rad=rad/180* math.pi
    clear_canvas()
    back.draw(TUK_WIDTH/2, TUK_HEIGHT/2)
    hand.draw(handx,handy)
    
    character.clip_composite_draw(frame*100, move*100 ,100,100 ,rad,'i',x,y,100,100)
    
    #character.clip_composite_draw(frame*100,move*100,100,100 ,rad,'v',x,y,100,100)
    update_canvas()
    delay(0.05)

def handle_events():
    global key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            key=1
        elif event.type == SDL_KEYDOWN and event.key== SDLK_ESCAPE:
            key=1
    
def run(x1,y1,x2,y2):
    frame=0
    #(y2-y1)/(x2-x1)*x + y1 -x1*(y2-y1)/(x2-x1)
    speed=20
    y=y1
    x=x1
    angle = math.atan2((y2-y1),(x2-x1))
    while 1:
        x +=speed*math.cos(angle)
        y +=speed*math.sin(angle)
        if x2-x1>0:
            draw_all(frame,1,x,y,0)
        else:
            draw_all(frame,0,x,y,0)
        frame = (frame+1)%8
        if x2-speed-1<=x<=x2+speed-1 and y2-speed-1<=y<=y2+speed-1:
            break

def run_reset():
    global x,y,handx,handy
    run(x,y,handx,handy)
    x , y = handx , handy
    handx=random.randrange(0,TUK_WIDTH)
    handy=random.randrange(0,TUK_HEIGHT)

cnt =0
while 1:
    
    run_reset()
    cnt+=1
    print(cnt)
    #delay(1)

    
close_canvas()
