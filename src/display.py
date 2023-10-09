from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_P4
from pimoroni import RGBLED


# Constants
RGB_GREEN = (0, 255, 0)
RGB_BLACK = (0, 0, 0)


class Display:
    FONT_HEIGHT = 8
    FONT_SCALE = 6
    SCALED_FONT_HEIGHT = FONT_HEIGHT * FONT_SCALE

    def __init__(self):
        self.display = PicoGraphics(
            display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_P4, rotate=0
        )
        self.black_pen = self.display.create_pen(*RGB_BLACK)
        self.green_pen = self.display.create_pen(*RGB_GREEN)
        self.bounds = self.display.get_bounds()
        self.led = RGBLED(6, 7, 8)
        self.clear_led()

    def clear_text(self):
        self.display.set_pen(self.black_pen)
        self.display.clear()
        self.display.update()

    def clear_led(self):
        self.led.set_rgb(*RGB_BLACK)

    def turn_led_on(self):
        self.led.set_rgb(*RGB_GREEN)

    def write_text(self, text: str):
        text_width = self.display.measure_text(text, scale=Display.FONT_SCALE)
        DISPLAY_WIDTH, DISPLAY_HEIGHT = self.bounds

        self.display.set_pen(self.green_pen)
        self.display.text(
            text,
            # Center the text horizontally
            int((DISPLAY_WIDTH - text_width) / 2),
            int(
                # Center the text vertically
                (DISPLAY_HEIGHT - Display.SCALED_FONT_HEIGHT)
                / 2
            ),
            scale=Display.FONT_SCALE,
        )
        self.display.update()
