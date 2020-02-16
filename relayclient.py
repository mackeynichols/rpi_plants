#! python3
# relayclient.py - class(es) to manage relays connected to an rpi
import RPi.GPIO as GPIO
import time
import logging

class RelayClient:
    def __init__(self, pin):
        # GPIO library init        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        
        self.pin = pin

        GPIO.setup(pin, GPIO.OUT)
        
        logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                            level=logging.DEBUG,
                            filename='./logs/relay.log')
        
        logging.info('Relay ' + str(self.pin) + ' initialized')
        
    def turn_on(self):
        GPIO.output(self.pin, GPIO.LOW)
        
    def turn_off(self):
        GPIO.output(self.pin, GPIO.HIGH)
        
    #def cycle(turn_on_for, wait_for):

    def cleanup(self):
        GPIO.cleanup()
        

if __name__ == '__main__':
    relay = RelayClient(17)
    relay.turn_on()
    time.sleep(3)
    relay.turn_off()
    relay.cleanup()
    