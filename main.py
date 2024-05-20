from badusb.command import Command

from board import *
import digitalio
import storage

noPayloadStart = False
noPayloadPin = digitalio.DigitalInOut(GP16)
noPayloadPin.switch_to_input(pull=digitalio.Pull.UP)
noPayloadStart = not noPayloadPin.value

if(noPayloadStart == True):
    print("Payload not delivered")
else:
    if __name__ == "__main__":
        Command().execute("payload.txt")
