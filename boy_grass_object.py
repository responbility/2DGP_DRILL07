import random
from pico2d import *

class Grass:


    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:

    def __init__(self):

        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Zombie:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 170  # ⭐️ 랜덤 위치에서 시작하도록 수정
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 2

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h

        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width, frame_height)  # 축소 없이 원본 크기로 그림


running = True
world = []


def reset_world():
    global running
    global world

    running = True
    world = []  # 월드 리스트 초기화

    # 잔디 객체 생성 및 추가
    grass = Grass()
    world.append(grass)

    # 11명의 소년 축구단 생성 및 추가
    for i in range(11):
        boy = Boy()
        world.append(boy)

    # ⭐️ Zombie 객체 추가
    zombie = Zombie()
    world.append(zombie)


def update_world():
    """월드 내 모든 객체의 상태를 업데이트"""
    for o in world:
        o.update()


def render_world():
    """월드 내 모든 객체를 화면에 그림"""
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def handle_events():
    """키보드 및 마우스 이벤트 처리"""
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# ===============================================
# 3. 메인 게임 루프
# ===============================================

open_canvas()

reset_world()  # 초기화 코드

while running:
    handle_events()  # 이벤트 처리
    update_world()  # 게임 로직
    render_world()  # 드로잉
    delay(0.05)  # 프레임 속도 조절

close_canvas()  # 종료 코드