# decimal_pin_pad_transmitter

from microbit import *
import radio

radio.on()
radio.config(channel=7)

pin = ''
n = 0

while True:

    x = len(pin)
    
    if button_a.was_pressed():
        if n < 5:
            n += 1
            if n is not 0:
                y = n - 1
                display.set_pixel(x, y, 9)
        else:
            for y in range(0, 5):
                display.set_pixel(x, y, 0)
            n = 0
    if button_b.was_pressed():
        pin += str(n)
        n = 0
        if len(pin) == 3:
            radio.send(pin)
            display.scroll(pin)
            pin = ''
            display.clear()
