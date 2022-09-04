import pygame
pygame.init()

DRAW_GRID_LINES = True

WIDTH = HEIGHT = 512
ROWS = COLS = 4
PIXEL_SIZE = WIDTH//ROWS

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

BG_COLOUR = BLACK

FPS = 60

def get_font(size):
    return pygame.font.SysFont("comicsans", size)
