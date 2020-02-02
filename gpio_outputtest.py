import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
pin = 4

GPIO.setup(pin, GPIO.OUT)

print("high!")
GPIO.output(pin, GPIO.HIGH)

time.sleep(3)

print("low!")
GPIO.output(pin, GPIO.LOW)
time.sleep(3)

GPIO.cleanup()