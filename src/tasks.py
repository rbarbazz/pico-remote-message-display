import asyncio
import random

from display import Display


SPEED = 60

display = Display()
lock = asyncio.Lock()


def split_text(text: str):
    lines = []
    current_line = ""

    for char in text:
        if not current_line:
            current_line = char
        elif display.fits_on_display(current_line + char):
            current_line += char
        else:
            lines.append(current_line.strip())
            current_line = char

    if current_line:
        lines.append(current_line)

    return lines


async def process_message(message: str):
    async with lock:
        # Wait one second to avoid blinking effect between messages
        await asyncio.sleep(1)

        # Split message into lines
        message_lines = split_text(message)
        max_lines = display.max_lines
        # Split the lines into screens based on max lines per screen value
        screens = [
            message_lines[i : i + max_lines]
            for i in range(0, len(message_lines), max_lines)
        ]

        display.turn_led_on()

        for screen in screens:
            for line_index, line in enumerate(screen):
                for i in range(len(line)):
                    display.write_text(line[: i + 1], line_index=line_index)
                    # Simulate human typing
                    await asyncio.sleep_ms(int(SPEED + SPEED * (random.random() - 0.5)))

            # Wait and move onto the next screen
            await asyncio.sleep(1)
            display.clear_text()

        await asyncio.sleep(2)
        display.clear_text()
        display.clear_led()
