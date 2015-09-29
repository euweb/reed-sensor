#!/usr/bin/env python

import time
import httplib
import RPi.GPIO as GPIO


# setup for raspberry pi 2 B
# RPi.GPIO board layout
GPIO.setmode(GPIO.BOARD)

# Pin 18 (GPIO 24)
PIN=18

# Counter
counter=2050.04

# Pin PIN as input, pull-up (3.3V)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def on_impulse(pin):
    global counter
    counter += 0.01
    print 'on impulse: ' + str(pin) + ' counter=' + str(counter) + " pinvalue=" + str(GPIO.input(PIN))

GPIO.add_event_detect(PIN, GPIO.FALLING, callback=on_impulse, bouncetime=200)
#GPIO.add_event_detect(PIN, GPIO.FALLING, callback=my_callback_two)

# polling in a loop, until interrupted by Ctrl-C
while 1:

 try:

  print "alive: "+ str(GPIO.input(PIN))

  # send counter
  #restConnection = httplib.HTTPConnection('127.0.0.1', 8080)
  #restConnection.request('PUT', '/rest/items/Gas_Meter/state', str(counter))
  #resultST = restConnection.getresponse()

  time.sleep(10)

 except KeyboardInterrupt:
     GPIO.remove_event_detect(PIN)
     GPIO.cleanup()

GPIO.remove_event_detect(PIN)
GPIO.cleanup()
