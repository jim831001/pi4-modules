#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print(mode)

pin = 7 

#GPIO.setup(pin, GPIO.OUT)
#GPIO.output(pin, GPIO.LOW)
#time.sleep(0.1)
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

print(GPIO.input(pin))

# Set to input
GPIO.setup(pin, GPIO.IN)

print(GPIO.input(pin))

while True:
    if GPIO.input(pin) == GPIO.LOW:
        print("GPIO LOW")
    else:
        print("GPIO HIGH")

GPIO.cleanup()
