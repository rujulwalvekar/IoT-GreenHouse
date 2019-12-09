import RPi.GPIO as gpio
import time


def wateringPlants():
    # read moisture

    gpio.setup(15, gpio.IN)
    value = gpio.input(15)
    if value == 1:
        # turn pump on for some seconds
        gpio.setup(17, gpio.OUT)
	gpio.output(17,gpio.LOW)
        time.sleep(5)
        gpio.output(17, gpio.HIGH)
        time.sleep(1)

if __name__ == '__main__':
    try:
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        while True:
            wateringPlants()
            time.sleep(1)
    except:
        gpio.cleanup()
