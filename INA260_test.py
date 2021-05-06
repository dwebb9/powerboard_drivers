import smbus
import time


# change address to correct address
bus = smbus.SMBus(1)
address = 0x45


while True:
    c_bus = bus.read_i2c_block_data(address,1)
    v_bus = bus.read_i2c_block_data(address,2)
    p_bus = bus.read_i2c_block_data(address,3)
    
    current = (c_bus[0]*256 + c_bus[1])*0.00125
    voltage = (v_bus[0]*256 + v_bus[1])*0.00125
    power = (p_bus[0]*256 + p_bus[1])*0.01
    
    if current > 20: current = 0
    print ("Current: ",current) #bus Volatage? 
    print ("Voltage: ",voltage) #address for current measurment
    print ("Power: ",power)

#     print ("Current",bus.read_i2c_block_data(address,1)) #bus Volatage? 
#     print ("Voltage",bus.read_i2c_block_data(address,2)) #address for current measurment
#     print ("Power",bus.read_i2c_block_data(address,3))



    time.sleep(1)
