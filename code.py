"""
Authors = Alec Autry, Sean Duffie
"""

#imports
import board
import digitalio
import time
import adafruit_hcsr04

# IR sensor - Always returns True unless triggered
IR = digitalio.DigitalInOut(board.GP15)
IR.direction = digitalio.Direction.INPUT
IR.pull = digitalio.Pull.UP

#Distance LEDS
GreenLED = digitalio.DigitalInOut(board.GP6)
GreenLED.direction = digitalio.Direction.OUTPUT

Yellow1LED = digitalio.DigitalInOut(board.GP7)
Yellow1LED.direction = digitalio.Direction.OUTPUT

Yellow2LED = digitalio.DigitalInOut(board.GP8)
Yellow2LED.direction = digitalio.Direction.OUTPUT

RedLED = digitalio.DigitalInOut(board.GP9)
RedLED.direction = digitalio.Direction.OUTPUT

GarageLights = digitalio.DigitalInOut(board.GP16)
GarageLights.direction = digitalio.Direction.OUTPUT

# Define Variables
distance: float = 0
ZONE1 = 15
ZONE2 = 25
ZONE3 = 35
ZONE4 = 45

# Ultrasonic HC-RS-4 -  
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP3, echo_pin = board.GP2, timeout=0.5)

while True:
    try:
        distance = sonar.distance
    except RuntimeError:
        pass

    print(distance)
    time.sleep(0.1)

    if distance > ZONE4:
        GreenLED.value = True
        Yellow1LED.value = False
        Yellow2LED.value = False
        RedLED.value = False

    elif distance > ZONE3:
        GreenLED.value = True
        Yellow1LED.value = True
        Yellow2LED.value = False
        RedLED.value = False

    elif distance > ZONE2:
        GreenLED.value = False
        Yellow1LED.value = True
        Yellow2LED.value = True
        RedLED.value = False

    elif distance > ZONE1:
        GreenLED.value = False
        Yellow1LED.value = False
        Yellow2LED.value = True
        RedLED.value = True

    else:
        GreenLED.value = False
        Yellow1LED.value = False
        Yellow2LED.value = False
        RedLED.value = True

    if IR.value is False:
        GarageLights.value = False
    else:
        GarageLights.value = True
