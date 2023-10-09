from display import Display
import asyncio

display = Display()
lock = asyncio.Lock()


async def process_message(message: str):
    async with lock:
        # Wait one second to avoid blinking effect between messages
        await asyncio.sleep(1)

        display.turn_led_on()
        display.write_text(message)
        await asyncio.sleep(5)

        display.clear()
        display.clear_led()
