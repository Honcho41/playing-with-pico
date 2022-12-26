include "pico_display.hpp"

using namespace pimoroni;

uint16_t buffer[PicoDisplay::WIDTH * PicoDisplay::HEIGHT];
PicoDisplay pico_display(buffer);

int main() {
    pico_display.init();

    // set the backlight to a value between 0 and 255
    // the backlight is driven via PWM and is gamma corrected by our
    // library to give a gorgeous linear brightness range.
    pico_display.set_backlight(100);

    while(true) {
        // detect if the A button is pressed (could be A, B, X, or Y)
        if(pico_display.is_pressed(pico_display.A)) {
            // make the led glow green
            // parameters are red, green, blue all between 0 and 255
            // these are also gamma corrected
            pico_display.set_led(0, 255, 0);
        }

        // set the colour of the pen
        // parameters are red, green, blue all between 0 and 255
        pico_display.set_pen(30, 40, 50);

        // fill the screen with the current pen colour
        pico_display.clear();

        // draw a box to put some text in
        pico_display.set_pen(10, 20, 30);
        Rect text_rect(10, 10, 150, 150);
        pico_display.rectangle(text_rect);

        // write some text inside the box with 10 pixels of margin
        // automatically word wrapping
        text_rect.deflate(10);
        pico_display.set_pen(110, 120, 130);
        pico_display.text("This is a message", Point(text_rect.x, text_rect.y), text_rect.w);

        // now we've done our drawing let's update the screen
        pico_display.update();
    }
}