#
# Reley Control Kao Tamorat
#

import time
import RPi.GPIO as io
import subprocess
#from subprocess import Popen

#Dismiss Warning State
io.setwarnings(False) 

#Define io For GPIO
io.setmode(io.BCM)

# Define Pin
btn_pin= 4
reley0_pin= 24

#Setup Reley Pin
io.setup(btn_pin,io.IN)
io.setup(reley0_pin,io.OUT)

#Prepare Reley To High
io.output(reley0_pin,io.LOW)

#Movie Path
movie_path = 'tamorat_reley.mp4'

#Start Loop
print("Kao Tamorat Reley Control Start...")
while True:
    if (io.input(btn_pin)):
        #Turn Light Off
        print("Start Power Off")
        io.output(reley0_pin, io.HIGH)
        time.sleep(1)
        print("Reley 0 Power Off")
        #Play Movie
        omxp = subprocess.Popen(["omxplayer","-o","hdmi",movie_path])
        time.sleep(50) #Movie Length
        #End Movie Turn Light On
        print("Power On")
        io.output(reley0_pin, io.LOW)
        #Wait Until Button Ready
        time.sleep(5)
#Ending
