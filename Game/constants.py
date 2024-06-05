import pygame;
import pygame.font;

pygame.init()

# This File defines all the constants used for Colours, Sizes,...

# Sizes
MOB_TYPES = ["Player","Aberga","Rocker"]
PLAYER_HEIGHT = 48
PLAYER_WIDTH = 32

ABERGA_HEALTH = 100
ABERGA_HEIGHT = 48
ABERGA_WIDTH = 32
ABERGA_SPEED = 2
ABERGA_RANGE = 51
ABERGA_DAMAGE = 5
ABERGA_STUN_COOLDOWN = 100

ROCKER_HEALTH = 100
ROCKER_HEIGHT = 48
ROCKER_WIDTH = 32
ROCKER_SPEED = 2
ROCKER_RANGE = 51
ROCKER_DAMAGE = 5
ROCKER_STUN_COOLDOWN = 100

RANGE = 50

# Game
FRAMES_PER_SECOND = 120
SCREEN_WIDTH = 1148
SCREEN_HEIGHT = 720
GAME_SCALE = 2

TILE_SIZE = 16 * GAME_SCALE
TILE_TYPES = 113
LEVEL_NAMES = ["HTL","HAK"]
MAIN_FONT = pygame.font.Font("Game/assets/fonts/MainFont.ttf",35)

# Menu
BUTTON_SCALE = 1

# Player - Stats
SPEED = 3
OFFSET = 12

PENCIL_SPEED = 10
P_DAMAGE_BASE = 10
P_DAMAGE_EXTRA = 5
P_HIT_COOLDOWN = 500 # in miliseconds

FIREBALL_SPEED = 4

# Item
COIN_SCALE = 1
POTION_SCALE = 2
PIZZA_SCALE = 1

FIREBALL_SCALE = 1

# Weapon
WEAPON_SCALE = 1.5

# Schanzensop
SHOP_WIDTH = 64
SHOP_HEIGHT = 64
SHOP_RANGE = 64
SHOP_TILE_SCALE = 4

#GUI
HEART_SCALE = 3


# Backend
ROWS = 150
COLS = 150
SCROLL_THRES = 200

# Colours
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
BACKGROUND = (204,204,204)
MENU_BG = (0,0,0)
WHITE = (255, 255, 255)
PANEL = (50,50,50)
YELLOW = (255,215,0)