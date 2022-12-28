# credit to trs15/PicoScroll - https://github.com/trs15/PicoScroll/blob/d126928ebbf60058736eb7fe4e4c0bfa21b3c492/block_breaker.py

import picoscroll
import time

# Initialise the board
picoscroll.init()


#height = 7, width = 17
width = picoscroll.get_width()
height = picoscroll.get_height()

gameboard = []

bar_height = 3
bar_width = 3 
    
def Create_game_board():
    #Get the width and height of the board
   
    #x = width = 17
    #y = height = 7
    global gameboard
    gameboard = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    print(gameboard[0][0])
    
    

    
    # print(len(boardcolumns))
    # print(boardcolumns)


def move_left():
    global gameboard
    bar_row = gameboard[17 - bar_height]
    print(bar_row)
    if(bar_row[0] != 1):
        for i in range(0,6):
            bar_row[i] = bar_row[i+1] # not plus 1, simply changed to equal the index to the left of it.
    bar_row[6] = 0
    print(bar_row)


def move_right():
    global gameboard
    bar_row = gameboard[17 - bar_height]
    print(bar_row)
    if(bar_row[6] != 1):
        for i in range(6,0,-1):
            bar_row[i] = bar_row[i-1]
    bar_row[0] = 0
    print(bar_row)
    

def read_array():
    global gameboard
    for i in range(0,width):
            for j in range(0,height):
                picoscroll.set_pixel(i, j, gameboard[i][j]*100)

def Game():
    alive = True
    read_array()

    #Gameloop
    while alive == True:

        if(picoscroll.is_pressed(picoscroll.BUTTON_Y) == True):
            move_right()
            while(picoscroll.is_pressed(picoscroll.BUTTON_Y) == True):
                this = True
        if(picoscroll.is_pressed(picoscroll.BUTTON_X) == True):
            move_left()
            while(picoscroll.is_pressed(picoscroll.BUTTON_X) == True):
                this = True
        print(gameboard[14])
        
        read_array()
        picoscroll.update()



Create_game_board()

Game()