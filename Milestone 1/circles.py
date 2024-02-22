#Task 4 - Circles pt1

import simplegui, random

COUNT = 0


def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'


def draw_handler(canvas):
    
    global COUNT
    if COUNT%1==0:
        canvas.draw_circle((200, 225), 30, 10, randCol(), randCol())
        canvas.draw_circle([200, 175], 30, 10, randCol(), randCol())
       
    COUNT+=1
    
frame = simplegui.create_frame('Testing', 400, 400)
frame.set_draw_handler(draw_handler)
frame.start()
    