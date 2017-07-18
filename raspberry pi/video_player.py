# Installation
# Replace the videos with your needed files. Make sure to follow the naming scheme, what ever video you want to play on a loop name it 'splash.mpv'
# Copy the 'code' folder to /home/pi/ directory.
# After the folder has been copied we must set it to auto start when the Pi boots.
# sudo nano /etc/rc.local
# and then replace the IP dummy script with
# sudo python /home/pi/code/video_player.py

#Casio projectors: casio
# XJ-UT310WN
# 3100 Lumens
# WXGA (1280 x 800) Native Resolution
# Ultra Short Throw 0.28:1 ratio
# Fixed Lens – Mirror System
# Hybrid Light Source
# in Config.txt DMT modes
# hdmi_group=1   CEA
# hdmi_group=2   DMT (choose this one)
# hdmi_mode=27   1280x800        reduced blanking
# hdmi_mode=28   1280x800  60Hz
# hdmi_mode=29   1280x800  75Hz
# hdmi_mode=30   1280x800  85Hz
# hdmi_mode=31   1280x800  120Hz reduced blanking

# hdmi_safe=1
# This is the same as adding the following lines together:
#
# hdmi_force_hotplug=1
# config_hdmi_boost=4
# hdmi_group=1
# hdmi_mode=1
# disable_overscan=0

#hdmi_force_hotplug=1 Use HDMI mode even if no HDMI monitor is detected


# External module imports
import time
import sys
import os
import subprocess
from subprocess import Popen
#import pygame



# Video assignment
movie1 = '/home/pi/lots/video/shasta.mp4'
movie2 = '/home/pi/lots/video/shasta_no_border.mp4'


#kills any active instance of OMXplayer on start
os.system('killall omxplayer.bin')

#this is what process it is looking for is running
process_name= "omxplayer.bin"

#Uses pygame to hide desktop
#Prevents user killing the process
#screen = pygame.display.set_mode((1024, 768), pygame.NOFRAME)
#pygame.mouse.set_visible(False)



while True:
    omxp = Popen(['omxplayer','-o','local',movie1])
    time.sleep(15)
    os.system('killall omxplayer.bin')
    time.sleep(1)
    omxp = Popen(['omxplayer','-o','local',movie2])
    time.sleep(15)
