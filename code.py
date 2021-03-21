import time
import board
import usb_hid

from digitalio import DigitalInOut, Direction, Pull

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button_1 = DigitalInOut(board.D0)
button_2 = DigitalInOut(board.D1)

button_1.direction = Direction.INPUT
button_2.direction = Direction.INPUT

button_1.pull = Pull.UP
button_2.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)

print("waiting for a pin press")

while True:
    # pull up means we have to check for False
    if not button_1.value:
        print("REC pressed")
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.R)
        time.sleep(0.05)
        keyboard.release(Keycode.CONTROL, Keycode.ALT, Keycode.R)
        time.sleep(1)
    if not button_2.value:
        print("Pause pressed")
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.P)
        time.sleep(0.05)
        keyboard.release(Keycode.CONTROL, Keycode.ALT, Keycode.P)
        time.sleep(1)