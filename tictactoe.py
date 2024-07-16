import pygame as pg,sys
from pygame.locals import *
import time

#init global variables
XO = 'x'
winner = None
draw = False
width = 400 #400 is the number of pixels for length
white = (255, 255, 255) #nums are variables for white
line_color = (10, 10, 10) #nums are variables for black

#init the game board
TTT = [[None]*3, [None]*3, [None]*3]

#init pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, width + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe!")

#loading images
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

#resizing images to window
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, width + 100))

def game_opening() :
    screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    #draws vertical lines for board
    pg.draw.line(screen, line_color, (width / 3, width), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, width), 7)
    #draws horizontal lines for board
    pg.draw.line(screen, line_color, (0, width / 3), (width, width / 3), 7)
    pg.draw.line(screen, line_color, (0, width / 3 * 2), (width, width / 3 * 2), 7)
    draw_status()

def draw_status() :
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    elif draw:
        message = 'Game Draw!'
    else:
        message = winner.upper() + " won!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)

    #copies rendered message to board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()