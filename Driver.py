import RPi.GPIO as GPIO
import time
from smbus import SMBus

bus = smbus.SMBus(1)
ARDUINO_address = 0x8 # address of arduino nano
bus = SMBus(1) #indicates /dev/ic2-1

numb = 1

print("Enter 1 for ON of 0 for OFF")

while numb == 1:
    
    ledstate = input(">>>>    ")
    
    if ledstate == "1":
        bus.write_byte(addr, 0x1) #switch it on
    elif ledstate == "0":
        bus.write_byte(addr, 0x0) #switch it off
    elif ledstate == "2":
        bus.write_byte(addr, 0x2)
    elif ledstate == "3":
        bus.write_byte(addr, 0x3)
    elif ledstate == "4":
        bus.write_byte(addr, 0x4)
    else:
        numb = 0