import pygame as py, sys
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

