from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

class Explosion:
    def __init__(self, position=Vector(500, 400), size=1):
        self.img= simplegui.load_image('https://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png')
        self.stepper=Vector(100, 100)
        self.point=Vector(self.stepper.x/2, self.stepper.y/2)
        self.dimension=Vector(900, 900)
        self.position=position
        self.change=1
        self.size=size
        
    def step(self):
        self.change+=1
        self.point.x+=self.stepper.x
        if self.point.x>self.dimension.x:
            self.point.x=self.stepper.x/2
            self.point.y+=self.stepper.y
            if self.point.y>self.dimension.y:
                self.point.y=self.stepper.y/2

        if self.change>78:
            return True
        else:
            return False

    def draw(self, canvas):
        canvas.draw_image(self.img, self.point.get_p(), self.stepper.get_p(), self.position.get_p(), self.stepper.__mul__(self.size).get_p() )
        
WIDTH=600
HEIGHT=600
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_canvas_background('white')

def randVector(initial_x, final_x, initial_y, final_y):
    v =Vector(random.randint(initial_x, final_x), random.randint(initial_y, final_y))
    return v

class Operator:
    def __init__(self):
        self.object=[]
        self.waste=[]
        self.speed=25
        self.timer = simplegui.create_timer(self.speed, self.timer_handler)
        self.timer.start()
        
        
    def timer_handler(self):
        size=random.randint(1, 2)
        v=randVector(0, WIDTH, 0, HEIGHT)
        self.object.append(Explosion(v, size/2))
        for i in self.object:
            if i.step():
                self.waste.append(i)
                self.object.remove(i)

    def clean(self):
        for y in self.waste:
            del y
        self.waste.clear()

    def draw(self, canvas):
        self.clean()
        for i in self.object:
            i.draw(canvas)
a=Operator()
frame.set_draw_handler(a.draw)
frame.start()
