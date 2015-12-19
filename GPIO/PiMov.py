#
# Movie Control
#

import time
import RPi.GPIO as GPIO
import subprocess
#from subprocess import Popen

#Dismiss Warning State
GPIO.setwarnings(False) 

#Define io For GPIO
GPIO.setmode(GPIO.BCM)

# Define Pin
btn_pin= 24
GPIO.setup(btn_pin, GPIO.IN)

#Movie Path
movie_path = 'hall1.mp4'
prev_input = 1

#Start Loop
print("Movie Control Start...")
while True:
  #take a reading
  input = GPIO.input(btn_input)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
  
  if (GPIO.input(btn_pin) == 0):
    #Play Movie
    omxp = subprocess.Popen(["omxplayer","-o","local",movie_path])
    time.sleep(1010) #Movie Length
    #Wait Until Button Ready
    time.sleep(10)
#Ending
