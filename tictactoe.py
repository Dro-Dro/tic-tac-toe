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
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, width), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, width), 7)
    #draws horizontal lines for board
    pg.draw.line(screen, line_color, (0, width / 3), (width, width / 3), 7)
    pg.draw.line(screen, line_color, (0, width / 3 * 2), (width, width / 3 * 2), 7)
    draw_status()

def draw_status() :
    global draw, white

    #messages for win/lose/draw states
    if winner is None :
        message = XO.upper() + "'s Turn"
    elif draw :
        message = 'Game Draw!'
    else :
        message = winner.upper() + " won!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)

    #copies rendered message to board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win() :
    global TTT, winner, draw

    #check for any winning rows
    for row in range (0, 3) :
        if ((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)) :
            #winning row found
            winner = TTT[row][0]
            #draw line through winning row
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1) * width / 3 - width / 6), (width, (row + 1) * width / 3 - width / 6 ), 4)
            break

    #check for any winning columns
    for col in range (0, 3) :
        if ((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)) :
            #winning col found
            winner = TTT[0][col]
            #draw line through winning col
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0), ((col + 1) * width / 3 - width / 6, width), 4)
            break

    #check for any winning diagonal
    if ((TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None)) :
        #winning left to right diagonal
        winner = TTT[0][0]
        #draw line through winning diagonal
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    elif ((TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None)) :
        #winning right to left diagonal
        winner = TTT[0][2]
        #draw line through winning diagonal
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    
    #check for draw
    if (all ([all(row) for row in TTT]) and winner is None) :
        draw = True
    draw_status()

def drawXO(row, col) :
    global TTT, XO

    #define row position
    if row == 1 :
        posx = 30
    elif row == 2 :
        posx = width / 3 + 30
    elif row == 3 :
        posx = width / 3 * 2 + 30

    #define column position
    if col == 1 :
        posy = 30
    elif col == 2 :
        posy = width / 3 + 30
    elif col == 3 :
        posy = width / 3 * 2 + 30

    #draws respective image to screen
    TTT[row - 1][col - 1] = XO
    if XO == 'x' :
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else : 
        screen.blit(o_img, (posy, posx))
        XO = 'x'

    pg.display.update()

def userClick() :
    #gets the coordinates of mouse click
    x, y = pg.mouse.get_pos()

    #gets column aka y coordinate of mouse click
    if (x < width / 3) :
        col = 1
    elif (x < width / 3 * 2) :
        col = 2
    elif (x < width) :
        col = 3
    else :
        col = None
    
    #gets row aka x coordinate of mouse click
    if (y < width / 3) :
        row = 1
    elif (y < width / 3 * 2) :
        row = 2
    elif (y < width) :
        row = 3
    else :
        row = None

    #draw img at user click position
    if (row and col and TTT[row - 1][col - 1] is None) :
        global XO

        #draws x or o on screen
        drawXO(row, col)
        check_win()

def reset_game() :
    global TTT, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None] * 3, [None] * 3, [None] * 3]

#running the game
game_opening()

#run game loop forever
while(True) :
    for event in pg.event.get() :
        if event.type == QUIT :
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN :
            #user clicked on screen
            userClick()
            if (winner or draw) :
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)