import random
from pico2d import *


# ===============================================
# 1. 게임 오브젝트 클래스 정의
# ===============================================

class Grass:
    """잔디 클래스: 움직이지 않는 배경 객체"""

    def __init__(self):
        # 객체가 생성될 때, 맨 처음 자동 호출되는 함수 (생성자)
        # 속성 (멤버 변수) 설정
        self.image = load_image('grass.png')

    def draw(self):
        """잔디를 화면에 그리는 행위"""
        self.image.draw(400, 30)

    def update(self):
        """잔디의 상태를 시간에 따라 변경하는 행위 (현재는 변경 없음)"""
        pass  # 현재 잔디는 상태 변경이 없으므로 비워둠


class Boy:
    """소년 클래스: 움직이는 캐릭터 객체"""

    def __init__(self):
        # 소년별로 시작 위치를 다르게 설정
        self.x, self.y = random.randint(100, 700), 90
        # 애니메이션 프레임도 소년별로 다르게 시작
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        """소년의 상태를 시간에 따라 변경하는 행위"""
        # 프레임을 순환시키고 (애니메이션)
        self.frame = (self.frame + 1) % 8
        # x 좌표를 증가시켜 이동 (행위)
        self.x += 5

    def draw(self):
        """소년을 화면에 그리는 행위"""
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


# ===============================================
# 2. 전역 변수 설정 및 초기화/종료 함수
# ===============================================

running = True
world = []  # 모든 게임 오브젝트를 담을 리스트 (강의 자료의 'world list')


def reset_world():
    """게임 월드 초기화: 객체들을 생성하고 world 리스트에 추가"""
    global running
    global world

    running = True
    world = []  # 월드 리스트 초기화

    # 잔디 객체 생성 및 추가
    grass = Grass()
    world.append(grass)

    # 소년 축구단 (11명) 생성 및 추가 (List Comprehension 이용)
    # team = [Boy() for i in range(11)]
    # world += team # 리스트 연결

    # 10명이 아닌, 강의 자료 마지막 리팩토링에 따라 11명으로 구현
    for i in range(11):
        boy = Boy()
        world.append(boy)


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

# 캔버스 열기
open_canvas()

# 초기화 코드
reset_world()

# 게임 루프 코드
while running:
    handle_events()  # 이벤트 처리
    update_world()  # 게임 로직 (객체들의 상호작용 시뮬레이션: 상태 변화)
    render_world()  # 드로잉 (그 결과를 보여줌: 렌더링)
    delay(0.05)  # 프레임 속도 조절

# 종료 코드
close_canvas()