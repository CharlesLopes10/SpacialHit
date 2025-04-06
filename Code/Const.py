# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level11Bg0': 0,
    'Level11Bg1': 1,
    'Level11Bg2': 2,
    'Level11Bg3': 3,
    'Level11Bg4': 4,
    'Level11Bg5': 5,
    'Level11Bg6': 6,
    'Level12Bg0': 0,
    'Level12Bg1': 1,
    'Level12Bg2': 2,
    'Level12Bg3': 3,
    'Level12Bg4': 4,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,

}

ENTITY_HEALTH = {
    'Level11Bg0': 999,
    'Level11Bg1': 999,
    'Level11Bg2': 999,
    'Level11Bg3': 999,
    'Level11Bg4': 999,
    'Level11Bg5': 999,
    'Level11Bg6': 999,
    'Level12Bg0': 999,
    'Level12Bg1': 999,
    'Level12Bg2': 999,
    'Level12Bg3': 999,
    'Level12Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level11Bg0': 0,
    'Level11Bg1': 0,
    'Level11Bg2': 0,
    'Level11Bg3': 0,
    'Level11Bg4': 0,
    'Level11Bg5': 0,
    'Level11Bg6': 0,
    'Level12Bg0': 0,
    'Level12Bg1': 0,
    'Level12Bg2': 0,
    'Level12Bg3': 0,
    'Level12Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100 # 100ms
TIMEOUT_LEVEL = 20000 # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# SCORE
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
