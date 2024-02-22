try:
    import simplegui, random, math
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# The Vector class
class Vector:

    # Initialiser
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns a string representation of the vector
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Tests the inequality of this vector and another
    def __ne__(self, other):
        return not self.__eq__(other)

    # Returns a tuple with the point corresponding to the vector
    def get_p(self):
        return (self.x, self.y)

    # Returns a copy of the vector
    def copy(self):
        return Vector(self.x, self.y)

    # Adds another vector to this vector
    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return self.copy().add(other)

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        return self.multiply(-1)

    def __neg__(self):
        return self.copy().negate()

    # Subtracts another vector from this vector
    def subtract(self, other):
        return self.add(-other)

    def __sub__(self, other):
        return self.copy().subtract(other)

    # Multiplies the vector by a scalar
    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def __mul__(self, k):
        return self.copy().multiply(k)

    def __rmul__(self, k):
        return self.copy().multiply(k)

    # Divides the vector by a scalar
    def divide(self, k):
        return self.multiply(1/k)

    def __truediv__(self, k):
        return self.copy().divide(k)

    # Normalizes the vector
    def normalize(self):
        return self.divide(self.length())

    # Returns a normalized version of the vector
    def get_normalized(self):
        return self.copy().normalize()

    # Returns the dot product of this vector with another one
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Returns the squared length of the vector
    def length_squared(self):
        return self.x**2 + self.y**2

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.multiply(2*self.dot(normal))
        self.subtract(n)
        return self

    # Returns the angle between this vector and another one
    def angle(self, other):
        return math.acos(self.dot(other) / (self.length() * other.length()))

    # Rotates the vector 90 degrees anticlockwise
    def rotate_anti(self):
        self.x, self.y = -self.y, self.x
        return self

    # Rotates the vector according to an angle theta given in radians
    def rotate_rad(self, theta):
        rx = self.x * math.cos(theta) - self.y * math.sin(theta)
        ry = self.x * math.sin(theta) + self.y * math.cos(theta)
        self.x, self.y = rx, ry
        return self

    # Rotates the vector according to an angle theta given in degrees
    def rotate(self, theta):
        theta_rad = theta / 180 * math.pi
        return self.rotate_rad(theta_rad)

    # project the vector onto a given vector
    def get_proj(self, vec):
        unit = vec.get_normalized()
        return unit.multiply(self.dot(unit))


    def randVector(initial_x, final_x, initial_y, final_y):
        v =Vector(random.randint(initial_x, final_x), random.randint(initial_y, final_y))
        return v


WIDTH=700

HEIGHT=600

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'




class ball:
    def __init__(self, position, velocity=Vector(0,0), radius=0 , colour='red' ):
        self.position=position
        if velocity==0:
            self.velocity=Vector(0,0)
        else:
            self.velocity=velocity
        self.radius=radius
        self.colour=colour



    def is_in(self, pos=Vector(0,0)):
        k=self.position.__sub__(pos)
        r=k.length()
        return r<=self.radius

    def update(self):
        self.position.add(self.velocity)


    def force(self,force=Vector(0,0)):
        self.velocity.add(force)

    def __delete__(self):
        del self.position
        del self.velocity
        del self.radius
        del self.colour


    def draw(self,canvas):


        canvas.draw_circle(self.position.get_p(), self.radius, 1, self.colour, self.colour)



class interaction:
    def __init__(self, ball=None, initial=True,):
        self.ball=ball

        self.initial=initial




    def point(self, pos):
        if self.initial:
            self.ball=(ball(pos, 0,random.randint(10,80) ,randCol() ))
            self.initial=False
        elif self.ball.is_in(pos):
            k=pos.__sub__(self.ball.position)
            self.ball.force(k.multiply(-0.3))

        else:
            self.ball.Velocity=Vector(0,0)



    def draw(self, canvas):
        if self.ball!=None:
            self.ball.update()
            self.ball.draw(canvas)






a=interaction()

def mouse_handler(Position):
        x=Position[0]
        y=Position[1]
        g=Vector(x,y)
        a.point(g)

def button_handler():
        k=a.ball
        a.ball=None
        k.__delete__()
        a.initial=True



frame = simplegui.create_frame(" Colours ", WIDTH , HEIGHT)
frame.set_draw_handler(a.draw)


frame.set_mouseclick_handler(mouse_handler)




button = frame.add_button('clear',button_handler)



frame.start ()
