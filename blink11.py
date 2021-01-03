#!/usr/bin/env python3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)

GPIO.setup(25, GPIO.OUT)

while True:

          if  GPIO.input(4)==1: 

                        GPIO.output(25, 0)  

          else:

                        GPIO.output(25, 1) 
