#! python3
# basic flask app to control the rpi

from flask import Flask, render_template, redirect, url_for
from rpi import relayclient, temphumiditysensorclient, cameraclient
app = Flask(__name__)

relay4 = relayclient.RelayClient(4)
relay17 = relayclient.RelayClient(17)
temphumiditysensor27 = temphumiditysensorclient.Sensor(27)
cameraclient = cameraclient.Camera()

@app.route('/')
def index():
    cameraclient.capture()
    return render_template('index.html', temp = temphumiditysensor27.get_measurements()['temperature'], humidity = temphumiditysensor27.get_measurements()['humidity'])

@app.route('/on')
def on():
    relay4.turn_on()
    relay17.turn_on()
    return redirect(url_for('index'))

@app.route('/off')
def off():
    relay4.turn_off()
    relay17.turn_off()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')