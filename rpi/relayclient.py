#! python3
# relayclient.py - class(es) to manage relays connected to an rpi
# Typically, these are connected to GPIO ports 4 and 17
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

    def get_status(self):
        return GPIO.input(self.pin)

        
    #def cycle(turn_on_for, wait_for):

    def switch(self):
        if self.get_status(): # If switch is off, switch it on 
            self.turn_on()
        elif not self.get_status(): # If switch is on, turn it off
            self.turn_off()
        

    def cleanup(self):
        GPIO.cleanup()
        

if __name__ == '__main__':
    relay = RelayClient(4)
    relay.switch()
    time.sleep(4)
    relay.switch()
    relay.cleanup()
    