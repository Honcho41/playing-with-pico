#V1.0 is a simple tree shape with twinkling lights

import time
import random
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

# background colour
BG = display.create_pen(0,0,0) # black
white = display.create_pen(255, 255, 255) # white

# the tree is split into 4 layers which decrese
# in width with each layer
# 
# dx sets the width descrease per layer
# dy sets the height of each layer and therefore the whole tree
dx = 15
dy = 50

# min and max size of the "baubles"
minr = 2
maxr = 4

# number of baubles per layer
bpl = 15

# created a class of bauble to help create shapes later
# x is position on x axis
# y is postion on y axis
# r is radius of shape
# dr is change in radius to show twinkling
class Bauble:
    def __init__(self, x, y, r, dr):
        self.x = x
        self.y = y
        self.r = r
        self.dr = dr

baubles = []

# bottom layer of tree creates a number of baubles with random attributes
# each layer's random position attributes are restrained by decreasing x axis
# limits
for i in range(0, bpl):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint(dx, WIDTH - dx - r),
            random.randint(HEIGHT - dy, HEIGHT),
            random.randint(minr,maxr),
            random.randint(-1,1)
        ))

# second layer
for i in range(bpl, bpl*2):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint((2*dx), WIDTH - (2*dx)),
            random.randint(HEIGHT - (2*dy), HEIGHT - dy),
            random.randint(minr,maxr),
            random.randint(-1,1),
        ))

# third layer
for i in range(bpl*2, bpl*3):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint((3*dx), WIDTH - (3*dx)),
            random.randint(HEIGHT - (3*dy), HEIGHT - (2*dy)),
            random.randint(minr,maxr),
            random.randint(-1,1),
        ))

# fourth layer
for i in range(bpl*3, bpl*4):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint((4*dx), WIDTH - (4*dx)),
            random.randint(HEIGHT - (4*dy), HEIGHT - (3*dy)),
            random.randint(minr,maxr),
            random.randint(-1,1),
        ))

# main program
while True:
    display.set_pen(BG)
    display.clear()
    
    # iterate through list of baubles and draw them
    for bauble in baubles:
        
        display.set_pen(white)
        display.circle(int(bauble.x), int(bauble.y), int(bauble.r))
    
    # push to display
    display.update()
    time.sleep(0.15)
    
    # iterate through each bauble and change radius to show twinkling
    for bauble in baubles:
        
        twinkle = bauble.r + bauble.dr
        display.set_pen(white)
        display.circle(int(bauble.x), int(bauble.y), int(twinkle))
        
    display.update()
    time.sleep(0.15)