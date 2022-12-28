import time
import picoscroll
import random
import _thread # used for multithreading so i can have a consistant fall speed

#initialise the board
picoscroll.init()

#Get the width and height of the board
# height and width flipped because normal board operation is landscape
height = picoscroll.get_width()
width = picoscroll.get_height()

# toned down so I don't burn out my retinas
shapebright = 50

# I'm going to start by getting shapes to light up on the screen
# first, practice getting a single pixel to fall down the screen

# global variables for my pixel starting point
pixy = 0
pixx = 3

# function for the pixel "shape"
def pix():
    # sets the initial position of the pixel
    global pixy
    global pixx
    picoscroll.set_pixel(pixy,pixx,shapebright) # (Height, Width, Brightness)
    picoscroll.update()
    
    # loop to listen for button presses
    while pixy <= 16:
        picoscroll.set_pixel(pixy,pixx,0)
        #pixy = pixy + 1
        picoscroll.set_pixel(pixy,pixx,shapebright)
        picoscroll.update()
        
        # move right when button X is pressed
        if picoscroll.is_pressed(picoscroll.BUTTON_X) == True and pixx > 0:
            picoscroll.set_pixel(pixy,pixx,0)
            pixx = pixx - 1
            picoscroll.set_pixel(pixy,pixx,shapebright)
            picoscroll.update()
            
        elif picoscroll.is_pressed(picoscroll.BUTTON_X) == True and pixx == 6:
            pixx = pixx
            picoscroll.set_pixel(pixy,pixx,shapebright)
            picoscroll.update()
            
        # move left when button Y is pressed
        elif picoscroll.is_pressed(picoscroll.BUTTON_Y) == True and pixx < 6:
            picoscroll.set_pixel(pixy,pixx,0)
            pixx = pixx + 1
            picoscroll.set_pixel(pixy,pixx,shapebright)
            picoscroll.update()
            
        elif picoscroll.is_pressed(picoscroll.BUTTON_Y) == True and pixx == 0:
            pixx = pixx
            picoscroll.set_pixel(pixy,pixx,shapebright)
            picoscroll.update()
        
        # min time between button presses
        time.sleep(0.1)

# seperate funtion to control the speed that shapes fall
def falling():
    global pixy
    global pixx
    while pixy < 16:
        
        time.sleep(1)
        pixy = pixy + 1
        
        # for loop turns off the LEDs on the board "behind" the falling shape
        for i in range(0, pixy):
            for j in range(0, width):
                picoscroll.set_pixel(i, j, 0)
        picoscroll.update()
        # printing variable for debugging purposes.
        print("height = " + str(height)," width = " + str(width) +"\n")
        print("x = " + str(pixx), " y = " + str(pixy))


# start the falling function
_thread.start_new_thread(falling,())

# start the shape function
while True:
    pix()