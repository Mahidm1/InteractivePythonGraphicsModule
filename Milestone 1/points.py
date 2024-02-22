#TASK 2 - Points
import simplegui

# Constants are written in capital letters
WIDTH = 700
HEIGHT = 500

# Handler to draw on canvas: 
# this function is called 60 times per second
def draw(canvas):
    canvas.draw_point([WIDTH/2, HEIGHT/2], 'Yellow')# Middle
    canvas.draw_point([WIDTH/700, HEIGHT/500], 'White') # Top left
    canvas.draw_point([WIDTH/700, 499], 'Red') # Bottom left
    canvas.draw_point([699, 499], 'White')# Bottom right
    canvas.draw_point([699, 1], 'Red')#Top Right

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Points", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()