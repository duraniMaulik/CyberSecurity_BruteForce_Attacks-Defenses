# if_three_pin_fails_wait_an_hour

from microbit import *

sleep(1000)

pin = '324'
fails = 0

while True:
    message = input("Enter PIN: ")

    if message == pin:
        fails = 0
        print("Access granted.")
    else:
        fails += 1
        print("Access denied.")
        if fails > 2:
            print("Oops, 3 fails in a row!")
            print("Try again in an hour.")
            sleep(3600000)
            fails = 0
