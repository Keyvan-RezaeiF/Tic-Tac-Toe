import pygame as pg, sys
from pygame.locals import *
import time

# Initializing global variables
turn = 'x'
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
        message = turn.upper() + "'s turn"
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

def check_win():
    global TTT, winner, draw

    # Check for winning rows
    for row in range(0, 3):
        if (TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None):
            # This row won
            winner = TTT[row][0]
            pg.draw.line(screen, (255, 0, 0), (0, (row+1)*height/3-height/6),
                            (width, (row+1)*height/3-height/6), 4)
            break

    # Check for winning columns
    for col in range(0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
            winner = TTT[0][col]
            pg.draw.line(screen, (255, 0, 0), ((col+1)*width/3-width/6, 0), 
                            ((col+1)*width/3-width/6, height), 4)
            break

    # Check for diagonal winners 
    # left --> right
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        winner = TTT[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
    # right --> left
    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        winner = TTT[0][2]
        pg.draw.line(screen, (255, 70, 70), (350, 50), (50, 350), 4)

    if (all([all(row) for row in TTT]) and winner is None):
        draw = True
    
    draw_status()

def draw_XO(row, col):
    global TTT, turn

    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = 2 * width / 3 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = 2 * height / 3 + 30
     
    TTT[row - 1][col - 1] = turn
    if turn == 'x':
        screen.blit(x_img, (posy, posx))
        turn = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        turn = 'x'
    
    pg.display.update()

def check_user_click():
    # Getting coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # Getting column of mouse click
    if x < width/3:
        col = 1
    elif x < 2 * width / 3:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None

    # Getting row of mouse click
    if y < height/3:
        row = 1
    elif y < 2 * height / 3:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None
        
    if row and col and TTT[row-1][col-1] is None:
        global turn

        # Draw X or O on the screen
        draw_XO(row, col)
        check_win()

def reset_game():
    global TTT, winner, turn, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None]*3, [None]*3, [None]*3]

def check_events():
    # watch for mouse events
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                pg.quit()
                sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            check_user_click()
            if (winner or draw):
                reset_game()

# Start the game
game_opening()

# Run the main loop for the game forever
while(True):
    check_events()    
    pg.display.update()
    CLOCK.tick(fps)