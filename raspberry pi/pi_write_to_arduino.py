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
ser.write("6:12,5:50") #pin 6, PWM 100
ser.write('\n')

print "Did write, now read"
x = ser.readline()
print "got '" + x + "'" #got '6:100'

ser.close()
