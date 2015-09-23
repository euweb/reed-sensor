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

def my_callback_one(channel):
    print('Callback one')
    print GPIO.input(PIN)

GPIO.add_event_detect(PIN, GPIO.BOTH, callback=my_callback_one, bouncetime=200)
#GPIO.add_event_detect(PIN, GPIO.FALLING, callback=my_callback_two)

# polling in a loop, until interrupted by Ctrl-C
while 1:

 try:

  print "alive"
  time.sleep(10)

 except KeyboardInterrupt:
     GPIO.remove_event_detect(PIN)
     GPIO.cleanup()

GPIO.remove_event_detect(PIN)
GPIO.cleanup()
