from random import randint
import time
import RPi.GPIO as GPIO

# set mode
GPIO.setmode(GPIO.BCM)

# out pins
pins_out = [21,16,12,25,24,18]
for pin in pins_out:
    GPIO.setup(pin, GPIO.OUT)

# loop forever 
while True:

    try:
        # light pin for 1 second
        for pin in pins_out:

            # rand wait
            wait = randint(1,3)

            # blink
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(wait)
            GPIO.output(pin, GPIO.LOW)

    except KeyboardInterrupt:
        # turn off all lights
        for pin in pins_out:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()            
