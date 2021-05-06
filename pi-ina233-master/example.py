#!/usr/bin/python3

''' In this example, we have two INA233's, at addresses 0x40 and 0x41
for a hypothetical solar battery charging system.
'''

from ina233 import INA233
import time

R_shunt_ohms = 670 # shunt resistor value in Ohms
I_max_amps =  0.1 # max expected current in Amps
R_shunt_ohms_2 = 1000 # shunt resistor value in Ohms

monitor1_current_total = 0
monitor2_current_total = 0
monitor3_current_total = 0
monitor4_current_total = 0

monitor1_voltage = 0
monitor2_voltage = 0
monitor3_voltage = 0
monitor4_voltage = 0

recorded_data = [0,0,0,0,0,0,0,0,0,0]
recorded_raw  = [0,0,0,0,0,0,0,0,0,0]
reverse_data  = [0,0,0,0,0,0,0,0,0,0]
monitor3_data = [0,0,0,0,0,0,0,0,0,0]
monitor4_data = [0,0,0,0,0,0,0,0,0,0]

bus = 1 # I2C bus
monitor1_address = 0x40 #address of INA233 connected to battery circuit
monitor2_address = 0x41 # address of INA233 connected to solar charging circuit
monitor3_address = 0x42 #address of INA233 connected to battery circuit
monitor4_address = 0x43 # address of INA233 connected to solar charging circuit


monitor1_ina233 = INA233(bus, monitor1_address)
monitor2_ina233 = INA233(bus, monitor2_address)
monitor3_ina233 = INA233(bus, monitor3_address)
monitor4_ina233 = INA233(bus, monitor4_address)

monitor1_ina233.calibrate(R_shunt_ohms, I_max_amps)
monitor2_ina233.calibrate(R_shunt_ohms, I_max_amps)
monitor3_ina233.calibrate(R_shunt_ohms_2, I_max_amps)
monitor4_ina233.calibrate(R_shunt_ohms_2, I_max_amps)

for i in range(0, 10, 1):

    temp = monitor1_ina233.getCurrentIn_mA()
    temp2 = monitor2_ina233.getCurrentIn_mA()
    temp3 = monitor3_ina233.getCurrentIn_mA()
    temp4 = monitor4_ina233.getCurrentIn_mA()

    monitor1_voltage += monitor1_ina233.getBusVoltageIn_V()
    monitor2_voltage += monitor2_ina233.getBusVoltageIn_V()
    monitor3_voltage += monitor3_ina233.getBusVoltageIn_V()
    monitor4_voltage += monitor4_ina233.getBusVoltageIn_V()

    monitor1_current_total += temp
    monitor2_current_total += temp2
    monitor3_current_total += temp3
    monitor4_current_total += temp4

    recorded_data[i] = temp
    reverse_data[i]  = temp2
    monitor3_data[i] = temp3
    monitor4_data[i] = temp4

    #recorded_raw[i]  = float(monitor1_ina233.getRaw())

    time.sleep(1)

#average data
Monitor1 = monitor1_current_total/10
Monitor2 = monitor2_current_total/10
Monitor3 = monitor3_current_total/10
Monitor4 = monitor4_current_total/10
M1_volt = monitor1_voltage/10
M2_volt = monitor2_voltage/10
M3_volt = monitor3_voltage/10
M4_volt = monitor4_voltage/10

#print funtions
print("Monitor 1")
print("Current: ", Monitor1)
print("Current Values: ", recorded_data)
print("Raw Current: ", recorded_raw)
print("Voltage: ", M1_volt)

print("Monitor 2")
print("Current: ", Monitor2)
print("Current Values: ", reverse_data)
print("Voltage: ", M2_volt)

print("Monitor 3")
print("Current: ", Monitor3)
print("Current Values: ", monitor3_data)
print("Voltage: ", M3_volt)

print("Monitor 4")
print("Current: ", Monitor4)
print("Current Values: ", monitor4_data)
print("Voltage: ", M4_volt)