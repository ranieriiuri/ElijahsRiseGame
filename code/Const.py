import pygame
import os

# B

BG1_PATHS = [
    './asset/Level1Bg0.png',
    './asset/Level1Bg1.png',
    './asset/Level1Bg2.png',
    './asset/Level1Bg3.png',
    './asset/Level1Bg4.png',
    './asset/Level1Bg5.png'
]

# P/ implantação posterior
BG2_PATHS = [
    './asset/Level1Bg2-0.png',
    './asset/Level1Bg2-1.png',
    './asset/Level1Bg2-2.png',
    './asset/Level1Bg2-3.png',
    './asset/Level1Bg2-4.png',
    './asset/Level1Bg2-5.png',
    './asset/Level1Bg2-6.png'
]

BG3_PATHS = [
    './asset/Level1Bg3-0.png',
    './asset/Level1Bg3-1.png',
    './asset/Level1Bg3-2.png',
    './asset/Level1Bg3-3.png',
    './asset/Level1Bg3-4.png'
]



# C

C_ORANGE = (255, 128, 0)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_MILITARY_GREEN = (102, 124, 51)
C_GRAY = (128, 128, 128)
C_GOLD = (255, 215, 0)


# E
EVENT_OBSTACLE = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_MB = pygame.USEREVENT + 3

ENTITY_SPEED = {
    'Level1Bg0':0,
    'Level1Bg1':1,
    'Level1Bg2':3,
    'Level1Bg3':0,
    'Level1Bg4':1,
    'Level1Bg5':2,
    'Player':4,
    'Tree':1,
    'Wind':7,
    'Dog':9,
    'MeatBread':1
}

ENTITY_HEALTH = {
    'Level1Bg0':999,
    'Level1Bg1':999,
    'Level1Bg2':999,
    'Level1Bg3':999,
    'Level1Bg4':999,
    'Level1Bg5':999,
    'Player': 200,
    'Dog':999,
    'Tree':999,
    'Wind':999,
    'MeatBread':1
}

ENTITY_DAMAGE = {
    'Level1Bg0':0,
    'Level1Bg1':0,
    'Level1Bg2':0,
    'Level1Bg3':0,
    'Level1Bg4':0,
    'Level1Bg5':0,
    'Player': 1,
    'Dog':60,
    'Tree':40,
    'Wind':90,
    'MeatBread':0
}
ENTITY_SCORE = {
    'Level1Bg0':0,
    'Level1Bg1':0,
    'Level1Bg2':0,
    'Level1Bg3':0,
    'Level1Bg4':0,
    'Level1Bg5':0,
    'Player': 0,
    'Dog':0,
    'Tree':0,
    'Wind':0,
    'MeatBread':0
}
ENTITY_VALUE = {
    'MeatBread': 5
}


# M
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}

# S
SPAWN_TIME = 2500 # 2.5s
MB_SPAWN_TIME = 6000 # 6s p criar MBs

# T
TIMEOUT_STEP = 1000  # 1s
TIMEOUT_LEVEL = 80000  # 80s (1min 20s)

# W
WIN_WIDTH = 800
WIN_HEIGHT = 480

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

#CONSTANTES USADAS EM EFEITOS ADICIONAIS
# Caminho base do projeto (pasta raiz)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))