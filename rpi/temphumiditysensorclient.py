#! python3
# temphumiditysensorclient.py - class(es) for managing DHT temp/humidity sensors

import Adafruit_DHT
import logging

class Sensor:
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin

        logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                            level=logging.DEBUG,
                            filename='./logs/temphumiditysensor.log')

        logging.info("Temperature and Humidity Sensor Initialized")

    def get_measurements(self):
        # returns temp in Celsius and Humidity as a percentage
        humidity, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        logging.info( "Humidity: " + str(humidity) + "% Temperature: " + str(temp) +"C" )
        return {"humidity": humidity, "temperature": temp}

if __name__ == "__main__":
    print(Sensor(27).get_measurements())