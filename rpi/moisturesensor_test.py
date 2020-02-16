import RPi.GPIO as GPIO
import time

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
pin = 4
# Set the GPIO pin to an input
GPIO.setup(pin, GPIO.IN)

while True:
    print(GPIO.input(pin)) # 1 for dry, 0 for wet

