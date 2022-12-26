import time
import random
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

BG = display.create_pen(40, 40, 40)
star = display.create_pen(250, 250, 25)
white = display.create_pen(255, 255, 255)

class Bauble:
    def __init__(self, x, y, r, dr):
        self.x = x
        self.y = y
        self.r = r
        self.dr = dr

#base layer x axis 0 - 134
#base layer y axis 218 - 239
# initialise shapes
baubles = []
for i in range(0, 10):
    r = random.randint(0, 2) + 3
    baubles.append(
        Bauble(
            random.randint(0, 134),
            random.randint(218, r + (HEIGHT - 2 * r)),
            r,
            2),
        )

while True:
    display.set_pen(BG)
    display.clear()

    for bauble in baubles:
        #bauble.r *= bauble.dr
        
        display.set_pen(white)
        display.circle(int(bauble.x), int(bauble.y), int(bauble.r))
        
        display.update()
        time.sleep(0.01)
