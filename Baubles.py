import time
import random
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

BG = display.create_pen(40, 40, 40)
star = display.create_pen(250, 250, 25)
white = display.create_pen(255, 255, 255)

dx = 15
dy = 35

minr = 2
maxr = 4

bpl = 15
class Bauble:
    def __init__(self, x, y, r, dr):
        self.x = x
        self.y = y
        self.r = r
        self.dr = dr

baubles = []

for i in range(0, bpl):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint(dx, WIDTH - dx - r),
            random.randint(HEIGHT - dy, HEIGHT),
            random.randint(minr,maxr),
            random.randint(-1,1)
        ))

for i in range(bpl, bpl*2):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint((2*dx), WIDTH - (2*dx)),
            random.randint(HEIGHT - (2*dy), HEIGHT - dy),
            random.randint(minr,maxr),
            random.randint(-1,1),
        ))

for i in range(bpl*2, bpl*3):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint((3*dx), WIDTH - (3*dx)),
            random.randint(HEIGHT - (3*dy), HEIGHT - (2*dy)),
            random.randint(minr,maxr),
            random.randint(-1,1),
        ))

for i in range(bpl*3, bpl*4):
    r = random.randint(0, 10) + 3
    baubles.append(
        Bauble(
            random.randint((4*dx), WIDTH - (4*dx)),
            random.randint(HEIGHT - (4*dy), HEIGHT - (3*dy)),
            random.randint(minr,maxr),
            random.randint(-1,1),
        ))

while True:
    display.set_pen(BG)
    display.clear()

    for bauble in baubles:
        
        display.set_pen(white)
        display.circle(int(bauble.x), int(bauble.y), int(bauble.r))
        
    display.update()
    time.sleep(0.15)
    
    for bauble in baubles:
        
        twinkle = bauble.r + bauble.dr
        display.set_pen(white)
        display.circle(int(bauble.x), int(bauble.y), int(twinkle))
        
    display.update()
    time.sleep(0.15)