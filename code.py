# Author: Alec Autry
# Example code for ESET 462:

#imports
import sys
import board
import digitalio
import busio
import time
import adafruit_hcsr04

# GPIO Pin = digitalio.DigitalInOut(board.GP#)


# IR sensor - Always returns True unless triggered
ir_OUT = digitalio.DigitalInOut(board.GP15)
ir_OUT.direction = digitalio.Direction.INPUT


#Distance LEDS
GreenLED = digitalio.DigitalInOut(board.GP6)
GreenLED.direction = digitalio.Direction.OUTPUT

Yellow1LED = digitalio.DigitalInOut(board.GP8)
Yellow1LED.direction = digitalio.Direction.OUTPUT

Yellow2LED = digitalio.DigitalInOut(board.GP7)
Yellow2LED.direction = digitalio.Direction.OUTPUT

RedLED = digitalio.DigitalInOut(board.GP9)
RedLED.direction = digitalio.Direction.OUTPUT

GarageLights = digitalio.DigitalInOut(board.GP16)
GarageLights.direction = digitalio.Direction.OUTPUT

# Define Virables
timepassed = 0.0
distance = 0.0
signalon = 0
signaloff = 0

#Ultrasonic Setup
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP3, echo_pin = board.GP2)

while True:
    try:
        distance = sonar.distance
        print(distance)
    except RuntimeError:
        distance = 0
    time.sleep(0.1)
    if distance == 0:
        RedLED.value = False
        Yellow1LED.value = False
        Yellow2LED.value = False
        GreenLED.value = False
    elif distance > 70:
        RedLED.value = True
        Yellow1LED.value = False
        Yellow2LED.value = False
        GreenLED.value = False

    elif distance > 50 and (distance < 70):
        RedLED.value = True
        Yellow1LED.value = True
        Yellow2LED.value = False
        GreenLED.value = False

    elif distance >25 and (distance < 50):
        RedLED.value = True
        Yellow1LED.value = True
        Yellow2LED.value = True
        GreenLED.value = False

    elif distance < 25:
        RedLED.value = True
        Yellow1LED.value = True
        Yellow2LED.value = True
        GreenLED.value = True
    if ir_OUT.value == False:
        GarageLights.value = True
    elif ir_OUT:
        GarageLights.value = False

