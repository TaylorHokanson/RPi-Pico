#!/usr/bin/env python

import time
from machine import Pin

led = Pin(25, Pin.OUT)

def flasher():
    led.value(1)
    time.sleep(.1)
    led.value(0)
    time.sleep(.4)
    
if __name__ == "__main__":
    while True:
        flasher()
