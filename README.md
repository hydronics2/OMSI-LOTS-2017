# OMSI-LOTS-2017

Arduino, Outie PWM Driver
 * LOTs Arduino PWM shield
 * Raspberry PI sends pin ID and PWM rate over serial data via USB cable
 * parsed into individual signals and drives mosfets with a PWM signal using the sparkfun mosfet shield
 * https://www.sparkfun.com/products/10618
 * 
 * 1:30 is pin 1, PWM 30
 * also accepts two or more values comma seperated up to 38 bytes
 * 1:30,5:254,9:75
 * terminated wiht a carraige return '/n'
 * 
 * Arduino PWM pins are 3,5,6,9,10,11

 * Disable Auto Reset on Serial connection:
 * Stick a 120 ohm resistor in the headers between 5v and reset on the arduino


Raspberry Pi sends PWM commands to the Arduino over Serial 115200
#find arduino serial using command: ls /dev/tty*
#might be dev/ttyACM0 or ttyACM1 or ttyUSB0

ser.write("6:12") #pin 6, PWM 100
ser.write('\n')
