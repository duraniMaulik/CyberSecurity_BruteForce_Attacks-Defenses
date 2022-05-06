# bank_vault_crack.py

from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)

digits = ['0','1']

display.show(Image.ARROW_W)

while True:
    if button_a.was_pressed():
        
        display.clear()

        for a in digits:
            for b in digits:
                for c in digits:
                    pin = ''.join([a, b, c])
                    
                    print("pin =", pin)

                    for x in range(0, len(pin)):
                        bit = int(pin[x])
                        brightness = bit * 9
                        display.set_pixel(x,4,9)
                        for y in range(0, 4):
                            display.set_pixel(x, y, brightness)

                    response = None
                    while response is None:
                        radio.send(pin)
                        sleep(100)
                        response = radio.receive()
                            
                    print(response)
                    if response == "Access granted.":
                        while True:
                            display.scroll(pin)

                    sleep(4000)
                    display.clear()
