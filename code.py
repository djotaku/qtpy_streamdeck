import time
import board
import usb_hid

from digitalio import DigitalInOut, Direction, Pull

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button_1 = DigitalInOut(board.D0)

button_1.direction = Direction.INPUT

button_1.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)

print("waiting for a pin press")

while True:
    # pull up means we have to check for False
    if not button_1.value:
        print("button 1 pressed")
        time.sleep(0.1)