import RPi.GPIO as gpio
import Adafruit_DHT
import time
threshold = 15
def checkTemp():
    # read remperature
    humidity, temperature = Adafruit_DHT.read_retry(11, 24)

    gpio.setup(10, gpio.OUT)
    if temperature > threshold:
        gpio.output(10, gpio.LOW)
    else:
        gpio.output(10, gpio.HIGH)

if __name__ == '__main__':
    try:
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        while True:
            checkTemp()
            time.sleep(5000)
    except:
        gpio.cleanup()
