import picoscroll
import time
import _thread

# Initialise the board
picoscroll.init()


#height = 7, width = 17
width = picoscroll.get_width()
height = picoscroll.get_height()

gameboard = []


shape_height = 16
shape_width = 3
    
def Create_game_board():
    #Get the width and height of the board
   
    #x = width = 17
    #y = height = 7
    global gameboard
    gameboard = [[0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

    #print(gameboard[0][0])
    
    

    
    # print(len(boardcolumns))
    # print(boardcolumns)

def move_left():
    global gameboard
    global shape_row
    global shape_height
    
    shape_row = gameboard[17 - shape_height]
    #print(shape_row)
    if(shape_row[0] != 1):
        for i in range(0,6):
            shape_row[i] = shape_row[i+1] # not plus 1, simply changed to equal the index to the left of it.
    shape_row[6] = 0
    read_array()
    print(shape_row)


def move_right():
    global gameboard
    global shape_row
    global shape_height
    
    shape_row = gameboard[17 - shape_height]
    #print(shape_row)
    if(shape_row[6] != 1):
        for i in range(6,0,-1):
            shape_row[i] = shape_row[i-1]
    shape_row[0] = 0
    read_array()    

def read_array():
    global gameboard
    for i in range(0,width):
            for j in range(0,height):
                picoscroll.set_pixel(i, j, gameboard[i][j]*100)

def falling():
    global shape_height
    
    while shape_height > 0:
        shape_height = shape_height - 1
        picoscroll.update()
        time.sleep(1)
        

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
        #print(gameboard[14])
        #print(shape_height)
        
        read_array()
        picoscroll.update()

_thread.start_new_thread(falling,())

Create_game_board()

Game()