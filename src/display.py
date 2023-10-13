import math

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_P4
from pimoroni import RGBLED

# Constants
RGB_GREEN = (0, 255, 0)
RGB_BLACK = (0, 0, 0)
FONT_HEIGHT = 8
FONT_SCALE = 4
SCALED_FONT_HEIGHT = FONT_HEIGHT * FONT_SCALE
PADDING = 10
LINE_HEIGHT = SCALED_FONT_HEIGHT + PADDING


class Display:
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

    @property
    def max_lines(self):
        _, display_height = self.bounds

        return math.floor(display_height / LINE_HEIGHT)

    def get_text_width(self, text: str):
        return self.display.measure_text(text, scale=FONT_SCALE)

    def fits_on_display(self, text: str):
        display_width, _ = self.bounds
        text_width = self.get_text_width(text=text)

        return display_width - PADDING * 2 - text_width >= 0

    def write_text(self, text: str, line_index: int):
        self.display.set_pen(self.green_pen)
        self.display.text(
            text,
            PADDING,
            (LINE_HEIGHT * line_index),
            scale=FONT_SCALE,
        )
        self.display.update()
