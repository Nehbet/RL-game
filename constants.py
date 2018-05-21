import libtcodpy as libtcod
import pygame

pygame.init()

#Game sizes
CAMERA_WIDTH = 800
CAMERA_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

#FPS LIMIT
GAME_FPS = 60

#Map limitations
MAP_WIDTH = 100
MAP_HEIGHT = 100
MAP_MAX_NUM_ROOMS = 25

#Room limitations
ROOM_MAX_HEIGHT = 7
ROOM_MIN_HEIGHT = 3
ROOM_MAX_WIDTH = 5
ROOM_MIN_WIDTH = 3

#Color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (100, 100, 100)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

#Game colors
COLOR_DEFAULT_BG = COLOR_GREY

#FOV SETTINGS
FOV_ALGO = libtcod.FOV_BASIC
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

#MESSAGE DEFAULTS
NUM_MESSAGES = 4

## DEFAULT FONTS ##
FONT_DEBUG_MESSAGE = pygame.font.Font("data/joystix.ttf", 16)
FONT_MESSAGE_TEXT = pygame.font.Font("data/joystix.ttf", 12)
FONT_CURSOR_TEXT = pygame.font.Font("data/joystix.ttf", CELL_HEIGHT)
