 from pico2d import *



class grass:

def _init_(self):

self.image = load_image('grass.png')

def draw(self):

self.image.draw(400, 30)

def update (self): pass



def reset_world(self):

grass.update()

global grass

pass



def render_world(self):

clear_canvas()

grass.draw()

update_canvas()







def handle_events():

global running

events = get_events()

for event in events:

if event.type == SDL_QUIT:

running = False

elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

running = False









open_canvas()



while running:

handle_events()

update_world()

render_world()

delay(0.05)



close_canvas()