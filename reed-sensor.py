#!/usr/bin/env python

import time
from datetime import datetime
import sys
import getopt
import RPi.GPIO as GPIO

# Pin 18 (GPIO 24)
PIN=18
RRDB_NAME='counter.rrd'

def main(argv):                          
    counter = None 
    logfile = None

    try:                                
        opts, args = getopt.getopt(argv, "hdc:f:", ["help","debug","counter=","logfile="])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt == '-d':
            global _debug
            _debug = 1
        elif opt == '-h':
            usage();
            sys.exit(0)
        elif (opt in ("-c", "--counter")): 
            try:
                counter = float(arg)
            except ValueError:
                print("counter not a number")
                sys.exit(2)               
        elif (opt in ("-f", "--logfile")): 
            logfile = arg               

    #try to get counter from database

    print counter
    print logfile
    try:
         test = CountProcessor(PIN,counter,RRDB_NAME,logfile)
         while 1:
             #global datetime
             print "alive: " + str(datetime.now()) +" input was: " + str(GPIO.input(PIN)) + " current: " + str(test.counter)
             time.sleep(10)
    except KeyboardInterrupt:
         GPIO.remove_event_detect(PIN)
         GPIO.cleanup()
         f.close()

def usage():
    print """
Usage:
    -h                   -   print this message
    -c <counter value>   -   initial value for the counter (step is always 0.01)
    -d                   -   debug mode (for future use)
    -f <logfile name>    -   store the counter events in a log file
    """


class CountProcessor:
    def __init__(self, pin, init_counter, rrdb, logfile):
        self.pin = pin
        self.counter = init_counter
        self.rrdb = rrdb
        self.logfile = logfile
        self.setup_gpio(pin)

    def setup_gpio(self,pin):
        # setup for raspberry pi 2 B
        # RPi.GPIO board layout
        GPIO.setmode(GPIO.BOARD)
        # Pin PIN as input, pull-up (3.3V)
        GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(PIN, GPIO.FALLING, callback=self.on_impulse, bouncetime=2000)
        print "setup"

    def on_impulse(self,channel):
        self.counter += 0.01
        now = str(datetime.now())
        print now + 'on impuxlse: ' + str(pin) + ' counter=' + str(counter) + " pinvalue=" + str(GPIO.input(self.pin))
        #self.logfile.write( str(datetime.now()) + ' ' + str(counter) + ' ' + str(GPIO.input(self.pin)) + '\n' )

if __name__ == "__main__":
    main(sys.argv[1:])