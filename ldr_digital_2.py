import RPi.GPIO as gpio
import datetime
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.IN)
gpio.setup(27,gpio.OUT)

def readTime():
    try:
        ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
	return ds1307.read_datetime()
	
    except:
        # alternative: return the system-time:
        return datetime.datetime.utcnow()
Time1=readTime()

while True:
	print gpio.input(18),Time1.hour 

	if gpio.input(18)==1:
		gpio.output(27,gpio.LOW)
	else:
		gpio.output(27,gpio.HIGH)
gpio.cleanup()