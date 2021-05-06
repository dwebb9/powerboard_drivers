import RPi.GPIO as GPIO
import time

import smbus

# change address to correct address
bus = smbus.SMBus(1)
address = 0x4c

#bus.write_byte_data(address,0,1)
#bus.write_byte_data(address,0,0)
#while True:
    #print("switch, switch, severus switch")
    #time.sleep(5)

print("Switch written to: 1")
bus.write_byte_data(address,0,1)
current = bus.read_byte_data(address,0)
print("Switches on right after write: ", current)
time.sleep(1)
current = bus.read_byte_data(address,0)
print("Switches on 1 second after write: ", current)

while True:
    bus.write_byte_data(address,0,1)
    time.sleep(1)
    c_bus = bus.read_byte_data(address,0)
    
    current = c_bus
    
#     if current > 20: current = 0
    print ("Switches on: ",current) #bus Volatage? 

    time.sleep(4)
    
    bus.write_byte_data(address,0,0)
    time.sleep(1)
    c_bus = bus.read_byte_data(address,0)
    
    current = c_bus
    
#     if current > 20: current = 0
    print ("Switches on: ",current) #bus Volatage?
    time.sleep(4)
