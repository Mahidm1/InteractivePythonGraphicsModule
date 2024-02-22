#TASK 3 - Lines
import simplegui

WIDTH = 700
HEIGHT = 500
COUNT= 0 

def draw_handler(canvas):
    global COUNT
    if COUNT%1==0 & COUNT < HEIGHT:
        
        canvas.draw_line([WIDTH, 0], [0, HEIGHT], 2, 'Blue')
        canvas.draw_line([WIDTH, HEIGHT], [(WIDTH/WIDTH-1), (0)], 2, 'Blue')
        canvas.draw_line([COUNT, 0], [(COUNT), (HEIGHT)], 1, 'Red')
    if COUNT == HEIGHT:
        COUNT = 0    
    COUNT+=1
    
   


frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.start()