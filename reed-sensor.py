#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

# setup for raspberry pi 2 B
# RPi.GPIO board layout 
GPIO.setmode(GPIO.BOARD)

# Pin 18 (GPIO 24)
PIN=18

# Pin PIN as input, pull-up (3.3V)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# polling in a loop, until interrupted by Ctrl-C
while 1:

 try:
  
  if GPIO.input(PIN):
    print('Input was HIGH')
  else:
    print('Input was LOW')
  
  time.sleep(1)

 except KeyboardInterrupt:
        GPIO.cleanup()
        
GPIO.cleanup()