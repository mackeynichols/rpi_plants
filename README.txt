README

General
===
GPIO.BCM means you're looking at GPIO pins' GPIO numbers ... not their "BOARD" number

Temperature and Humidity Sensor
===
The sensors are called DHT11s
They require a py library called Adafruit_DHT to be read from
The DHT11 has 3 pins:
 the + goes to a 5v on the pi
 the - goes to a grnd on the pi
 the 'out' goes to a gpio pin on the pi
    in gpio_inpouttest.py, this is pin 7 (GPIO number 4)

reference:
https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
	

Moisture Sensor
===
Moisture sensor has 3 wires between pi and "center" piece
 VCC goes to 3.3v
 GND goes to GND
 DO goes to a GPIO pin
    in moisturesensor_test.py, this is pin 7 (GPIO number 4) 

reference:
https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc



Relay
===
The relay is just a switch; REMEMBER it doesnt supply any power, it just connects and disconnects the input circuit(s) its connected to
It has minimum 3 wired connected to the rpi:
 VCC goes to 5v
 GND goes to GND
 InX (1-4) goes to some GPIO pin

The Relay has 4 circuits it can control... one for each box
Looking at the relay such that each box's writing is right-side-up:
 Connect the TOP 2 "nodes" to the input circuit means the circuit is default ON
 Connect the BOTTOM 2 "nodes" to the input circuit means the circuit is default OFF
