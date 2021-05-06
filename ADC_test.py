import RPi.GPIO as GPIO
import time

import smbus

# change address to correct address
bus = smbus.SMBus(1)
address = 0x4b
#config in binary = 0b1000010010000011
config_dec = 33923

config = [int(config_dec/256), config_dec%256]

#print("config: ", config)

bus.write_i2c_block_data(address,1,config)

while True:
    #bus.write_byte_data(address,0,1)
    #c_bus = bus.read_byte_data(address,0)
    #v_bus = bus.read_byte_data(address,1)
    
    v_bus = bus.read_i2c_block_data(address,0)
#     p_bus = bus.read_i2c_block_data(address,3)
    
    #current = c_bus
    #voltage = v_bus
#     current = (c_bus[0]*256 + c_bus[1])*0.00125
    voltage = (v_bus[0]*256 + v_bus[1])>>3
#     power = (p_bus[0]*256 + p_bus[1])*0.01
    
#     if current > 20: current = 0
    #print ("Current: ",current) #bus Volatage?
    print ("Voltage: ", voltage*0.0014)

    time.sleep(2)
    
    #bus.write_byte_data(address,0,0)
    c_bus = bus.read_i2c_block_data(address,1)
    
#     v_bus = bus.read_i2c_block_data(address,2)
#     p_bus = bus.read_i2c_block_data(address,3)
    
#    current(0) = bin(c_bus).replace("0b", "")
    
    current = (c_bus[0]*256 + c_bus[1])
#     voltage = (v_bus[0]*256 + v_bus[1])*0.00125
#     power = (p_bus[0]*256 + p_bus[1])*0.01
    
#     if current > 20: current = 0
    #print ("current: ",c_bus)#bin(current)) #bus Volatage?
    time.sleep(2)

resetPin = 24
GPIO.setmode(GPIO.BCM)
#GPIO.setup(resetPin, GPIO.OUT)
#GPIO.output(resetPin, GPIO.LOW)

time.sleep(1)
GPIO.output(resetPin, GPIO.HIGH)
time.sleep(1)
GPIO.output(resetPin, GPIO.LOW)

