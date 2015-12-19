#
# PIR Sound Control
# update 18.12.15
# v 1.0

import os
import time
import RPi.GPIO as GPIO
import random
#import subprocess
from subprocess import Popen

#Dismiss Warning State
GPIO.setwarnings(False) 

#Define io For GPIO
GPIO.setmode(GPIO.BCM)

# Define Pin
pir_pin= 24
GPIO.setup(pir_pin, GPIO.IN, GPIO.PUD_DOWN)

#Movie Path
movie1 = '/home/pi/PiMov/panja_1.mp3'
movie2 = '/home/pi/PiMov/panja_2.mp3'
movie3 = '/home/pi/PiMov/panja_3.mp3'

previous_state = False
current_state = False

#Start Loop

#clear screen
os.system('printf "\033c"')

print("PIR Sound Control Start...")

while True:
    time.sleep(0.1)
    
    #take a reading
    previous_state = current_state
    current_state = GPIO.input(pir_pin)
    
    #if the last reading was low and this one high, print
    if current_state != previous_state:
        print("Bounce Detected")
        #update previous input
        previous_state = current_state
        
        #slight pause to debounce
        time.sleep(0.05)
        if (GPIO.input(pir_pin) == 1):
            print("GPIO Detected")
            #Start random selection
            ranMov = random.randint(1,4)
            if(ranMov == 1) :
                print('play : 1')
                omxp = Popen(["omxplayer", "-o","local", movie1])
                time.sleep(60)
                #clear screen
                os.system('printf "\033c"')
                print('GPIO Ready')
                
            if(ranMov == 2) :
                print('play : 2')
                omxp = Popen(["omxplayer", "-o","local", movie2])
                time.sleep(60)
                #clear screen
                os.system('printf "\033c"')
                print('GPIO Ready')
                
            if(ranMov == 3) :
                print('play : 3')
                omxp = Popen(["omxplayer", "-o","local", movie3])
                time.sleep(60)
                #clear screen
                os.system('printf "\033c"')
                print('GPIO Ready')
#Ending
