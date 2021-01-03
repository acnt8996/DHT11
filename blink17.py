#!/usr/bin/env python3
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)
count=0
while (count<10):
    print("turn on LED")
    LEDon = GPIO.output(11, 1)   
    time.sleep(0.5)
    print("turn off LED")
    LEDoff = GPIO.output(11,0)   
    time.sleep(0.5)
    count+=1

