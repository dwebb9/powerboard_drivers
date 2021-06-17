import RPi.GPIO as GPIO
import time
from smbus import SMBus
import lcm
import power_board

bus = SMBus(1)
ARDUINO_address = 0x8 # address of arduino nano
ADC1_address = 0x4b   # address of ADC 1
ADC2_address = 0x5b   # address of ADC 2

# Configure ADC
# config in binary = 0b1000010010000011
config_dec = 33923

config = [int(config_dec/256), config_dec%256]
bus.write_i2c_block_data(ADC1_address,1,config)
bus.write_i2c_block_data(ADC2_address,1,config)

#set up LCM
lc = lcm.LCM()

# initialize message to Arduino
numb = 1

print("Enter Arduino Input: ")

while numb == 1:

    # Arduino update
    ledstate = input(">>>>    ")
    
    if ledstate == "0":
        bus.write_byte(ARDUINO_address, 0x0) # all pins off
    elif ledstate == "1":
        bus.write_byte(ARDUINO_address, 0x1) # all pins on
    elif ledstate == "2":
        bus.write_byte(ARDUINO_address, 0x2) # Large SSR pin on
    elif ledstate == "3":
        bus.write_byte(ARDUINO_address, 0x3) # Large SSR pin off
    elif ledstate == "4":
        bus.write_byte(ARDUINO_address, 0x4) # DCDC24 pin on
    elif ledstate == "5":
        bus.write_byte(ARDUINO_address, 0x5) # DCDC24 pin off
    elif ledstate == "6":
        bus.write_byte(ARDUINO_address, 0x6) # DCDC12 pin on 
    elif ledstate == "7":
        bus.write_byte(ARDUINO_address, 0x7) # DCDC12 pin off
    else:
        numb = numb                          # do nothing

    # Battery ADC monitoring 
    ADC1_v = bus.read_i2c_block_data(ADC1_address,0)
    voltage1 = (ADC1_v[0]*256 + ADC1_v[1])>>3
    ADC2_v = bus.read_i2c_block_data(ADC2_address,0)
    voltage2 = (ADC2_v[0]*256 + ADC2_v[1])>>3


    time.sleep(2)
    
    ADC1_c = bus.read_i2c_block_data(ADC1_address,1)
    current1 = (ADC1_c[0]*256 + ADC1_c[1])
    ADC2_c = bus.read_i2c_block_data(ADC2_address,1)
    current2 = (ADC2_c[0]*256 + ADC2_c[1])
    time.sleep(2)

    

    print ("ADC1 Voltage: ", voltage1*0.0014)
    print ("ADC2 Voltage: ", voltage2*0.0014)
    print ("ADC1 Current: ", current1)
    print ("ADC2 Current: ", current2)