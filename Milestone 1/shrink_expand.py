#Task 4 - Circles pt2
import simplegui 

# Define globals
HEIGHT = 400
WIDTH = 400
ball_radius = 50
COUNT = 0
increasing = False

def draw(canvas):
    canvas.draw_point([WIDTH/2, HEIGHT/2], 'Yellow')
    
        
# Draw handler
    global COUNT, ball_radius, increasing
    if COUNT%1==0:
        canvas.draw_circle([WIDTH/2, HEIGHT/2],ball_radius,1,"Blue","Black")
    if ball_radius == 10:
        increasing = True
    if increasing == True:
        ball_radius+=1
    if ball_radius == 50:
        increasing = False
    if increasing == False:
        ball_radius -=1
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

  

# Start the frame animation
frame.start()