import pygame
import os

# B

BG_IMAGE_PATHS = [
    './asset/Level1Bg0.png',
    './asset/Level1Bg1.png',
    './asset/Level1Bg2.png',
    './asset/Level1Bg3.png',
    './asset/Level1Bg4.png'
]


# C

C_ORANGE = (255, 128, 0)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_MILITARY_GREEN = (102, 124, 51)
C_GRAY = (128, 128, 128)
C_GOLD = (255, 215, 0)

# E
EVENT_ENEMIES = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player': 3,
    'Tree': 1,
    'Bird': 2,
    'Wind': 2,
    'Dog':1
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player': 300
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player': 1,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player': 0
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
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 20000  # 20s
TIMEOUT_LEVEL = 40000  # 40s

# W
WIN_WIDTH = 600
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