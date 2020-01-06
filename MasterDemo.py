import RPi.GPIO as gpio
import time
import datetime
import Adafruit_DHT

#pin-10 : Humidity and Temp-Output
#pin-24 : Humidity and Temp-Input
#pin-14 : Moisture(Watering Plants input)
#pin-04 : Watering Plants output
#pin-18 : LDR input
#pin-27 : LED O/P
#
#
#***********For event change .hour to .second everywhere***** Verify
def checkTemp():
    # read remperature
    humidity, temperature = Adafruit_DHT.read_retry(11, 24)
    threshold = 20

    if temperature > threshold:
        gpio.output(10, gpio.LOW) #Start fan
    else:
        gpio.output(10, gpio.HIGH)

def readTime():
    try:
        ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
        return ds1307.read_datetime()

    except:
        # alternative: return the system-time:
        return datetime.datetime.now()



def CheckLightIntensity():
    if gpio.input(18)==1 and 8 <= readTime().hour <= 19:#Assume 1 for no light
            gpio.output(27,gpio.LOW)#Assume Low output leads to LED ON from relay
    else:
            gpio.output(27,gpio.HIGH)



def water():

    gpio.output(4,gpio.LOW)

def nowater():

    gpio.output(4,gpio.HIGH)



if __name__ == '__main__':
    #try:
    
    
        
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(14, gpio.IN)
    gpio.setup(4,gpio.OUT)
    gpio.setup(10, gpio.OUT)

    gpio.setup(18, gpio.IN)
    gpio.setup(27,gpio.OUT)
    sleeper=False
    start=time.monotonic()
    while True:
        if gpio.input(14)==1:# and readTime().hour>=16 :#Uncomment for setting motor to start on appropriate hour
            print("1==Water")
            gpio.output(4,gpio.LOW)#Assume Low starts motor
                  
        elif gpio.input(14)==0:
            print("2==NoWater")
            gpio.output(4,gpio.High)
            sleeper=True
        checkTemp()
            #print (gpio.input(18),Time1.hour )
        CheckLightIntensity()
        if (sleeper==True):
            #time.sleep(1800)
	    time.sleep(10)

   # except:
    #    gpio.cleanup()
