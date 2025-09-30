from pico2d import *
import random

class Boy:
    def __init__(self):
    self.x, self.y = random.randint(100, 700), 90
    slef.frame = 0
    self.image = load_image('run_animation.png')


class Ball:
    def __init__(self):
        self.imgae = load image('ball21x21.png')
#  공 유닛

class   grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def.draw(self)
        self.image.draw(400, 30)
    def update(self): pass