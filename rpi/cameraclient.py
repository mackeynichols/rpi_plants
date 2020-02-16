#! python3
# cameraclient.py - client for the picamera

import picamera
import logging
import os

class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1024, 768)

        logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                            level=logging.DEBUG,
                            filename='./logs/camera.log')

        logging.info("Pi Camera initialized")

    def capture(self):
        filename = 'plants.jpg'
        os.remove(filename)
        self.camera.capture( filename )
        logging.info("Picture taken: " + filename)

if __name__ == "__main__":
    Camera().capture()

        