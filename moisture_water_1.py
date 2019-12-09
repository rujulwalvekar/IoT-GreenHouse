import RPi.GPIO as gpio
import time


def wateringPlants():
    # read moisture
	value = gpio.input(14)
	if value == 1:
        # turn pump on for some seconds
		gpio.setup(4, gpio.OUT)
		gpio.output(4, gpio.LOW)
		time.sleep(5)
		gpio.output(4, gpio.HIGH)
		time.sleep(1)

if __name__ == '__main__':
	try:
		gpio.setwarnings(False)
		gpio.setmode(gpio.BCM)
		gpio.setup(14, gpio.IN)
		gpio.setup(4, gpio.OUT)
		while True:
			wateringPlants()
			time.sleep(1)
	except:
		gpio.cleanup()
