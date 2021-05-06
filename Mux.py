import RPi.GPIO as GPIO
import time

import smbus

bus = smbus.SMBus(1)
address = 0x77
address2 = 0x40

resetPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(resetPin, GPIO.OUT)
GPIO.output(resetPin, GPIO.LOW)

GPIO.output(resetPin, GPIO.HIGH)

mux_register = 0b00000001
mux_register2 = 0b00000010
bus.write_byte_data(address,0,mux_register)
    

while True:
    c_bus = bus.read_i2c_block_data(address2,1)
    v_bus = bus.read_i2c_block_data(address2,2)
    p_bus = bus.read_i2c_block_data(address2,3)
    
    current = (c_bus[0]*256 + c_bus[1])*0.00125
    voltage = (v_bus[0]*256 + v_bus[1])*0.00125
    power = (p_bus[0]*256 + p_bus[1])*0.01
    
    print("Current monitor 1")
    if current > 20: current = 0
    print ("Current: ",current) #bus Volatage? 
    print ("Voltage: ",voltage) #address for current measurment
    print ("Power: ",power)
    
    time.sleep(1)
    
    #bus.write_byte_data(address,0,mux_register2)
    #c_bus = bus.read_i2c_block_data(address2,1)
    #v_bus = bus.read_i2c_block_data(address2,2)
    #p_bus = bus.read_i2c_block_data(address2,3)
    
    #current = (c_bus[0]*256 + c_bus[1])*0.00125
    #voltage = (v_bus[0]*256 + v_bus[1])*0.00125
    #power = (p_bus[0]*256 + p_bus[1])*0.01
    
    #print("Current monitor 2")
    #if current > 20: current = 0
    #print ("Current: ",current) #bus Volatage? 
    #print ("Voltage: ",voltage) #address for current measurment
    #print ("Power: ",power)
    
    #bus.write_byte_data(address,0,mux_register)
    time.sleep(1)
    
    

#resetPin = 24
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(resetPin, GPIO.OUT)
#GPIO.output(resetPin, GPIO.LOW)

# time.sleep(1)
# GPIO.output(resetPin, GPIO.HIGH)
# time.sleep(1)
# GPIO.output(resetPin, GPIO.LOW)

