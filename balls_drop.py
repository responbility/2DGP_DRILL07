import random
from pico2d import *

class   grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__ (self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
         self.image= load_image()('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 150

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass




open_canvas()




while running:
    handle_events()
    update_world()
    render_world()


    delay(0.05)

close_canvas()