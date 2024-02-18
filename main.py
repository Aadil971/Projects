import urequests 
import time
import network
import final_lights

ssid = 'airuc-guest'
password = 'YOUR WIFI PASSSWORD HERE'


def connect():
    # Connect to WLAN
    # Connect function from https://projects.raspberrypi.org/en/projects/get-started-pico-w/2
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
try:
    connect()
except KeyboardInterrupt:
    machine.reset()



r = urequests.get("https://api.sunrisesunset.io/json?lat=51.078621&lng=-114.136719")
# Most APIs will return JSON, which acts like a Python dictionary
data = r.json()["results"]
sunrise = data['sunrise'].split(":")
print(sunrise)


for key, value in data.items():
    print(key,value)
# We need to close the response so that the Pi Pico does not crash

r.close()
