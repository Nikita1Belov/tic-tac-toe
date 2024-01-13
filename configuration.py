import pygame.font
pygame.font.init()

# frequency
FPS = 60

# font config
FONT_SIZE = 30
FONT_BUTTON_SIZE = 36
FONT_COMICS = pygame.font.SysFont('comicsansms', FONT_SIZE)
FONT_BUTTON = pygame.font.SysFont('arial', FONT_BUTTON_SIZE)

# music
MUSIC_WAY = "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/music.mp3"

# Ai player
AI = "AI"

# sizes of cell of board
CELL_MARGIN = 7.5  # gap between frame and cells
CELL_WIDTH = 190
CELL_HEIGHT = 190

# sizes of game window
GAME_WIDTH = 600  # width of game window
GAME_HEIGHT = 600  # height of game window
TITLE = "tic-tac-toe"

BACKGROUND_IMAGE = "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/backend.png"

IMAGE_PATH_BUTTON_BLUE = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/blue_button.jpg"
HOVER_IMAGE_PATH_BUTTON_BLUE = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/blue_button_hover.jpg"
IMAGE_PATH_BUTTON_RED = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/red_button.jpg"
HOVER_IMAGE_PATH_BUTTON_RED = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/red_button_hover.jpg"
IMAGE_PATH_BUTTON_YELLOW = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/yellow_button.jpg"
HOVER_IMAGE_PATH_BUTTON_YELLOW = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/yellow_button_hover.jpg"
IMAGE_PATH_BUTTON_GREEN = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/green_button.jpg"
HOVER_IMAGE_PATH_BUTTON_GREEN = \
    "/Users/nikitabelov/Documents_files/IT_и_физ-мат/Python/tic-tac-toe/sources/green_button_hover.jpg"

# sizes of global window
MESSAGE_HEIGHT = 150
WINDOW_WIDTH = GAME_WIDTH  # width of global window
WINDOW_HEIGHT = GAME_HEIGHT + MESSAGE_HEIGHT  # height of global window

# coordinates of text fields
X = GAME_WIDTH/2  # the middle of the window game
X_LABEL = GAME_WIDTH/2 - 120
X_BUTTON = GAME_WIDTH/2 - 150
X_BUTTON_COUPLE_1 = GAME_WIDTH/2 - 160
X_BUTTON_COUPLE_2 = GAME_WIDTH/2 + 40
X_LABEL_STAT = GAME_WIDTH/2 - 200
X_LABEL_M = GAME_WIDTH/2 - 170

Y_LABEL_1 = 50
Y_BUTTON_1 = 100
Y_STAT = 150
Y_BUTTON_2 = 200
Y_BUTTON_3 = 300
Y_BUTTON_4 = 400
Y_BUTTON_5 = 500
Y_BUTTON_6 = 600

# width-height
WIDTH_1 = 300
WIDTH_2 = 180
WIDTH_3 = 120
WIDTH_ML = 400
WIDTH_TOP = 100

HEIGHT = 50
HEIGHT_2 = 55
HEIGHT_T = 46

# RGB
YELLOW = (255, 255, 0)
BLUE = (0, 191, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 127)
WHITE = (255, 255, 255)
PEACH_PUFF = (255, 218, 185)
ROYAL_BLUE = (65, 105, 225)
ORANGE = (255, 102, 0)
GRAY = (128, 128, 128)

# list of key_objects
KEY_OBJ = [pygame.K_1, pygame.K_4, pygame.K_5,
           pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]
