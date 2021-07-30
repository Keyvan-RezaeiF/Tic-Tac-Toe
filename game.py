import pygame as pg, sys
from pygame.locals import *
import time

# Initializing global variables
XO = 'x'
winner = None
draw = False
width, height = 400, 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# Tic Tac Toe 3*3 board
TTT = [[None]*3, [None]*3, [None]*3]

# Initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Loading the images
opening_img = pg.image.load('images\\tic tac opening.png')
x_img = pg.image.load('images\X.png')
o_img = pg.image.load('images\O.png')

# Resizing images
opening_img = pg.transform.scale(opening_img, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))

def game_opening():
    screen.blit(opening_img, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    # Drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (2 * width / 3, 0), (2 * width / 3, height), 7)
    # Drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, 2 * height / 3), (width, 2 * height / 3), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Game draw!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # Copy the rendered message onto the board
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

    