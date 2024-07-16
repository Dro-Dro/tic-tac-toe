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
