import pygame as pg, sys
from pygame.locals import *
import time

# Initialize global variables.
XO = 'x'
winner = None
draw = False
width, height = 400, 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# Tic Tac Toe 3*3 board
TTT = [[None]*3, [None]*3, [None]*3]

# Initialize pygame window.
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")
