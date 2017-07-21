#find arduino serial using command: ls /dev/tty*
#might be dev/ttyACM0 or ttyACM1 or ttyUSB0

#Disable Auto Reset on Serial connection:
#Stick a 120 ohm resistor in the headers between 5v and reset on the arduino



#!/usr/bin/env python
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

print "Serial is open: " + str(ser.isOpen())

print "Now Writing"
comands = []
comands.append(1)  # Channel 1
comands.append(8)  # Light 1 function
comands.append(2)  # Channel 2
comands.append(250)  # Light 1 Brightness
comands.append(3)  # Channel 3
comands.append(250)  # Light 1 Mode
comands.append(4)  # Channel 4
comands.append(8)  # Light 2 function
comands.append(5)  # Channel 5
comands.append(250)  # Light 2 Brightness
comands.append(6)  # Channel 6
comands.append(250)  # Light 2 Mode
comands.append(7)  # Channel 7
comands.append(8)  # Light 3 function
comands.append(8)  # Channel 8
comands.append(250)  # Light 3 Brightness
comands.append(9)  # Channel 9
comands.append(250)  # Light 3 Mode
for i in comands:
    ser.write(str(comands[i]))
ser.close()
