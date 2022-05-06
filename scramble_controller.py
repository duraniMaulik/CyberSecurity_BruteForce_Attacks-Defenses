# wirelessControllerStrengthened.py

from microbit import *
import radio

radio.on()
radio.config(channel=3,length=64)

sleep(1000)

def scramble(text, encrypt):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789{},': "
    crypta = "RDNJOEGKZFAYLBXIWQHVTMSPCU9876543210{},': "
    result = ""
    
    if encrypt is False:
        temp = alpha
        alpha = crypta
        crypta = temp

    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]

    return result
 
''' Script starts from here... '''

print("\nSpeeds are -100 to 100\n")

while True:
    try:
        vL = int(input("Enter left speed: "))
        vR = int(input("Enter right speed: "))
        ms = int(input("Enter ms to run: "))

        dictionary = {  }
        dictionary['vL'] = vL
        dictionary['vR'] = vR
        dictionary['ms'] = ms

        packet = str(dictionary)
    
        print("Send: ", packet)
        packet = scramble(packet, True)
        print("Send Encrypted: ", packet)
        radio.send(packet)
    
        print()

    except:
        print("Error in value entered.")
        print("Please try again. \n")


