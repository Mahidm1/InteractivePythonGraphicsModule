import simplegui
import random

# The Vector class
class Vector:
    # Initialiser
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Adds another vector to this vector
    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def _add_(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtracts another vector from this vector
    def subtract(self, other):
        return self.add(-other)

    def _sub_(self, other):
        return Vector(self.x - other.x, self.y - other.y)

# The Ball class
class Ball:
    # Initialiser
    def __init__(self, position, velocity, radius, colour):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.colour = colour

    # Draws the ball on the canvas
    def draw(self, canvas):
        canvas.draw_circle((self.position.x, self.position.y), self.radius, 1, self.colour, self.colour)

    # Updates the position of the ball
    def update(self):
        self.position.add(self.velocity)
        self.radius -= 1
        if self.radius < 1:
            self.radius = 1

# Create a list to store the balls
balls = []

#Creat random colour
def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'



# Timer event handler to add a new ball to the canvas every 0.1 seconds
def add_ball():
    position = Vector(300,300)
    velocity = Vector(random.randrange(-5, 6), random.randrange(-5, 6))
    radius = random.randrange(10, 51)
    colour = randCol()
    balls.append(Ball(position, velocity, radius, colour))

# Draw event handler
def draw(canvas):
    # Remove balls that are outside the canvas or have a radius less than or equal to 1
    remove_balls = []
    for ball in balls:
        if (ball.position.x + ball.radius < 0 or ball.position.x - ball.radius > 600 or
            ball.position.y + ball.radius < 0 or ball.position.y - ball.radius > 600 or
            ball.radius <= 1):
            remove_balls.append(ball)
        else:
            ball.draw(canvas)
            ball.update()
    for ball in remove_balls:
        balls.remove(ball)

# Create a frame and register the draw event handler
frame = simplegui.create_frame("Ball animation", 600, 600)
frame.set_draw_handler(draw)

frame.start()
timer = simplegui.create_timer(100, add_ball)
timer.start()