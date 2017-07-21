# Installation


# /etc/rc.local does not work with feh.......................
# After the folder has been copied we must set it to auto start when the Pi boots.
# sudo nano /etc/rc.local
# and then replace the IP dummy script with
# sudo python /home/pi/lots/video_player.py


#added to autostart file /home/pi/.config/lxsessions/LXDE-pi/autostart
#line added: python /home/pi/lots/video_player.py &

#~/.config/lxsession/LXDE/autostart is unique to the currently logged on user
# had to use exact file locations for the images
#Check if the /home/pi/.config/lxsession/LXDE-pi/autostart file exists. If it exists, it will be used instead of /etc/xdg/lxsession/LXDE-pi/autostart.
#View logs (after reboot) in /home/pi/.xsession-errors:
# this log seems to be best: cd /home/pi/.cache/lxsession/LXDE-pi/run.log

#remove mouse:
#sudo apt-get install unclutter
#sudo nano ~/.config/lxsession/LXDE/autostart
#add @unclutter -display :0 -noevents -grab

#sudo apt-get install feh
#sudo apt-get install xdotool

#Screen Blanking (working)
# edit your script that's starting X. In the default build with lightdm the file to edit is
# /etc/lightdm/lightdm.conf
# in the SeatDefaults section it gives the command for starting the X server
# which is modified to get it to turn off the screen saver as well as dpms
#   [SeatDefaults]
#   xserver-command=X -s 0 -dpms

# force to 1280x800
#sudo nano /boot/config.txt
#hmdi_group=2

#Casio projectors: casio
# XJ-UT310WN
# 3100 Lumens
# WXGA (1280 x 800) Native Resolution
# Ultra Short Throw 0.28:1 ratio
# Fixed Lens – Mirror System
# Hybrid Light Source
# in Config.txt DMT modes
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
# hdmi_group=1 (CEA for TVs in lieu of monitors... wrong)
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
movie1 = '/home/pi/lots/video/mayan_test_.mp4'
movie2 = '/home/pi/lots/video/mayan_test_static.mp4'
movie3 = '/home/pi/lots/video/shasta_test.mp4'
movie4 = '/home/pi/lots/video/shasta_test_static.mp4'

time.sleep(1)

print("python script started")

#this mouse script moves the mouse so it doesn't continually activate the task bar
#sudo apt-get install xdotool
m1 = ['bash', '/home/pi/lots/moveMouse.sh']
bash = subprocess.Popen(m1)

#kills any active instance of OMXplayer on start
os.system('killall omxplayer.bin')
os.system('killall feh')

#this is what process it is looking for is running
process_name= "omxplayer.bin"

#Uses pygame to hide desktop
#Prevents user killing the process
#screen = pygame.display.set_mode((1024, 768), pygame.NOFRAME)
#pygame.mouse.set_visible(False)



while True:
    feh = Popen(['feh','-F','/home/pi/lots/three.jpg'])
    time.sleep(20)
    os.system('killall feh')
    time.sleep(.5)
    omxp = Popen(['omxplayer','-o','local',movie1])
    time.sleep(5)
    os.system('killall omxplayer.bin')
    time.sleep(.5)
    feh = Popen(['feh','-F','/home/pi/lots/three.jpg'])
    time.sleep(20)
    os.system('killall feh')
    time.sleep(.5)
    omxp = Popen(['omxplayer','-o','local',movie2])
    time.sleep(5)
    os.system('killall omxplayer.bin')
    time.sleep(.5)
    # omxp = Popen(['omxplayer','-o','local',movie3])
    # time.sleep(30)
    # os.system('killall omxplayer.bin')
    # time.sleep(1)
    # omxp = Popen(['omxplayer','-o','local',movie4])
    # time.sleep(30)
    # os.system('killall omxplayer.bin')
    # time.sleep(1)
