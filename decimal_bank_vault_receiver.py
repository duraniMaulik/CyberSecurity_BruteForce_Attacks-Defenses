# decimal_bank_vault_receiver

from microbit import *
import radio
import random

radio.on()
radio.config(channel=7)

pin = '324'

while True:

    display.show(Image.SQUARE_SMALL)
    
    message = radio.receive()
    
    if message:
        pin_entered = str(message)

        if pin_entered == pin:
            radio.send("Access granted.")
            for n in range(4):
                display.show(Image.YES)
                sleep(1000)
                display.clear()
                sleep(200)
        else:
            radio.send("Access denied.")
            display.show(Image.NO)
            sleep(3000)

        display.clear()    
