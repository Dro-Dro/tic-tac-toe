import pygame as pg,sys
from pygame.locals import *
import time

#init global variables
XO = 'x'
winner = None
draw = False
width = 400 #400 is the number of pixels for length
height = 400
white = (255, 255, 255) #nums are variables for white
line_color = (10, 10, 10) #nums are variables for black

#init the game board
TTT = [[None]*3, [None]*3, [None]*3]


