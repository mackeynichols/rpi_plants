import RPi.GPIO as GPIO
import Adafruit_DHT
import time


sensor = Adafruit_DHT.DHT11
pin = 4 # GPIO Pin 4 is position 7 on the pi: it's 4th from the top on the inside row of pins

while True:
    humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    print( 'Temp: {} C -- Humidity: {} %'.format(temp, humidity) )

GPIO.cleanup()