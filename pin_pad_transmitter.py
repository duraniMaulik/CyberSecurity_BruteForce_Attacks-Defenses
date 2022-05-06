# pin_pad_transmitter.py

from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)

pin = ''
n = 0

while True:

    x = len(pin)
    b = n * 9
    
    display.set_pixel(x,4,9)
    for y in range(0, 4):
        display.set_pixel(x, y, b)

    if button_a.was_pressed():
        n = n + 1
        n = n % 2
    if button_b.was_pressed():
        pin += str(n)
    if x == 3:
        radio.send(pin)
        display.scroll(pin)
        pin = ''
        n = 0
        display.clear()
