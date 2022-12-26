# V3.0 gives multicoloured baubles

import time
import random
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

# set the colours
BG = display.create_pen(0,0,0)
star = display.create_pen(250, 250, 25)
white = display.create_pen(255, 255, 255)
red = display.create_pen(255, 0, 0)
green = display.create_pen(11, 255, 3)
blue = display.create_pen(3, 19, 255)

# list of colours to randomly iterate through later
colours = [star, white, red, green, blue]

# the tree is split into 4 layers which decrese
# in width with each layer
# 
# dx sets the width descrease per layer
# dy sets the height of each layer and therefore the whole tree
# mid and top are used as reference points to draw the star
dx = 15
dy = 50
mid = int((WIDTH-1)/2)
top = int(HEIGHT-dy*4)

# min and max size of the "baubles"
minr = 1
maxr = 3

# number of baubles per layer
bpl = 25

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

# empty list to hold the baubles that I'll create in a min
baubles = []

# bottom layer of tree creates a number of baubles with random attributes
# each layer's random position attributes are restrained by decreasing x axis
# limits
for i in range(0, bpl):
    baubles.append(
        Bauble(
            random.randint(dx, WIDTH - dx),
            random.randint(HEIGHT - dy, HEIGHT - maxr),
            random.randint(minr,maxr),
            random.randint(-2,2)
        ))
# second layer
for i in range(bpl, bpl*2):
    baubles.append(
        Bauble(
            random.randint((2*dx), WIDTH - (2*dx)),
            random.randint(HEIGHT - (2*dy), HEIGHT - dy),
            random.randint(minr,maxr),
            random.randint(-2,2),
        ))

# third layer
for i in range(bpl*2, bpl*3):
    baubles.append(
        Bauble(
            random.randint((3*dx), WIDTH - (3*dx)),
            random.randint(HEIGHT - (3*dy), HEIGHT - (2*dy)),
            random.randint(minr,maxr),
            random.randint(-2,2),
        ))

# fourth layer
for i in range(bpl*3, bpl*4):
    baubles.append(
        Bauble(
            random.randint((4*dx), WIDTH - (4*dx)),
            random.randint(HEIGHT - (4*dy), HEIGHT - (3*dy)),
            random.randint(minr,maxr),
            random.randint(-2,2),
        ))
#main program
while True:
    display.set_pen(BG)
    display.clear()
    
    # draw the star
    display.set_pen(star)    
    display.polygon([
      (mid, top-20),
      (mid+4, top-16),
      (mid+10, top-14),
      (mid+4, top-10),
      (mid, top+7),
      (mid-3, top-10),
      (mid-9, top-14),
      (mid-3, top-16)
       
    ])

    # draw the baubles and randomly select a colour for each on each loop
    # no need for a twinkling loop this time,
    # the colour change has the same effect
    for bauble in baubles:
        
        seq = random.choice(colours)
        display.set_pen(seq)
        display.circle(int(bauble.x), int(bauble.y), int(bauble.r))
          
    display.update()
    time.sleep(0.2)
