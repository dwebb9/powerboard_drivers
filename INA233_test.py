import smbus
import time


# change address to correct address
bus = smbus.SMBus(1)
address = 0x48

Voltage = 5
Rload = 60*10**6

Rshunt = 100
MaximumExpectedCurrent = Voltage/Rload
Current_LSB = 50*10**(-9)

CAL = 0.00512/(Current_LSB*Rshunt)

m_current = 1/Current_LSB
m_volt = 8
m_vshunt = 4

r_current = -6
r_volt = 2
r_vshunt = 5

CAL_block = [int(CAL)%256, int(int(CAL)/256)]
bus.write_i2c_block_data(address,0XD4,CAL_block)
time.sleep(1)
CAL_input = bus.read_i2c_block_data(address, 0XD4)

while True:
    c_bus = bus.read_i2c_block_data(address,137,)
    v_bus = bus.read_i2c_block_data(address,136,)
    p_bus = bus.read_i2c_block_data(address,151,)
    
    current = (c_bus[1]*256 + c_bus[0])*Current_LSB
    voltage = (v_bus[1]*256 + v_bus[0])*0.00125
    power = (p_bus[1]*256 + p_bus[0])*Current_LSB*25
    
    print ("Current block: ", c_bus)
    print ("Voltage block: ", v_bus)
    print ("Current: ",current)
    print ("Voltage: ",voltage)
    print ("Power: ",power)

    time.sleep(1)
    
    
    #print ("MaximumExpectedCurrent: ", MaximumExpectedCurrent)
# print ("CAL: ", CAL)
# print ("CAL block: ", CAL_block)
# print ("CAL_input", CAL_input)
# print ("Current_LSB: ", Current_LSB)
# print ("Max Voffset: 10e-6")
# print ("VOffset: ", MaximumExpectedCurrent*Rshunt)

