Reed sensor
==========

## Introduction

This script is used to read the state from one GPIO pin of raspberry pi. The pin my be connected to a reed sensor for detection of an open door or for counting impulses of a gas meter.

## Installation

The script uses GPIO library from here: https://pypi.python.org/pypi/RPi.GPIO for convenient access of the GPIO pins.
To install the library on Raspbian do following steps in a terminal window:

 - `sudo apt-get update`
 - `sudo apt-get install python-dev`
 - `sudo apt-get install python-rpi.gpio`

After you did the above steps put the script in a directory on the raspberry.

## Wiring Pi

As long as we enabled internal pull-up resistor, we can simple connect the read sensor to GPIO pin defined in the script and to a GND pin (e.g. pin 6).  

## Running

Run `sudo python reed-sensor.py` in the terminal. The script reads the state of the pin every second and writes it to the console. To terminate the program press Ctrl-C
