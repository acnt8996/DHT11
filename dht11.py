#!/usr/bin/python
import time
import Adafruit_DHT
 
GPIO_PIN = 4
 
try:
    print("push Ctrl-C can stop")
    while True:
        h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
        if h is not None and t is not None:
            print("tem={0:0.1f}C hum={1:0.1f}%".format(t, h))
        else:
            print("fail")
        time.sleep(10)
except KeyboardInterrupt:
    print("end")
