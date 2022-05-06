# wirelessReceiverStrengthened.py

from cyberbot import *
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

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        print("Encrypted: ", packet)
        packet = scramble(packet, False)
        print("Decrypted: ", packet)

        dictionary = eval(packet)

        vL = dictionary['VL']
        vR = dictionary['VR']
        ms = dictionary['MS']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)


