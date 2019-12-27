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

def checkTemp():
    # read remperature
    humidity, temperature = Adafruit_DHT.read_retry(11, 24)
    threshold = 20

    if temperature > threshold:
        gpio.output(10, gpio.LOW)
    else:
        gpio.output(10, gpio.HIGH)

def readTime():
    try:
        ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
        return ds1307.read_datetime()

    except:
        # alternative: return the system-time:
        return datetime.datetime.utcnow()
Time1=readTime()


def CheckLightIntensity():
    if gpio.input(18)==1:
            gpio.output(27,gpio.LOW)
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

    start=time.monotonic()
    while True:
        val=int(time.monotonic()-start)
        if val%6==0 and  gpio.input(14)==1 :
            print("1==")
            gpio.output(4,gpio.HIGH)
            checkTemp()
            CheckLightIntensity()
            
        elif val%6==1:
            print("2==")
            gpio.output(4,gpio.LOW)
            checkTemp()
            #print (gpio.input(18),Time1.hour )

        CheckLightIntensity()


#            wateringPlants()
#            time.sleep(1)
   # except:
    #    gpio.cleanup()
