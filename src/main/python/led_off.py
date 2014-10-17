import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(18, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
