import simplegui

SHEET_URL = "http://www.cs.rhul.ac.uk/courses/CS1830/sprites/runnerSheet.png"
SHEET_WIDTH = 1440
SHEET_HEIGHT = 1480
SHEET_COLUMNS = 6
SHEET_ROWS = 5

class Spritesheet:
    def __init__(self, imgurl, width, height, columns, rows):
        self.imgurl = imgurl
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        
        
            # Calculate frame dimension
        self._init_dimension()

        # Set up frame index
        self.frame_index = [2, 1]

        # Create a clock for sprite animation
        self.clock = Clock()

    def _init_dimension(self):
        self.frame_width = self.width / self.columns
        self.frame_height = self.height / self.rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

    def _update_index(self):
        if self.clock.transition(10):
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            if self.frame_index[0] == 0:
                self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas):
        self._update_index()
        self.clock.tick()
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)
        dest_centre = (300, 150)
        # doesn't have to be same aspect ratio as frame!
        dest_size = (100, 100)

        img = simplegui.load_image(self.imgurl)

        canvas.draw_image(img,
                            source_centre,
                            source_size,
                            dest_centre,
                            dest_size)
class Clock:
    def __init__(self):
        self.time = 0
    def tick(self):
        self.time += 1
    def transition(self, frame_duration):
        if self.time % frame_duration == 0:
            return True
        else:
            return False
    
frame = simplegui.create_frame("Sprite", 600, 300)
sheet = Spritesheet(
SHEET_URL,
SHEET_WIDTH, SHEET_HEIGHT,
SHEET_COLUMNS, SHEET_ROWS
)
frame.set_draw_handler(sheet.draw)

frame.start()



    

