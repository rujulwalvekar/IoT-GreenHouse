import time
import Adafruit_DHT as DHT1
import sys
import urllib.request

import threading
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def DHT():
	threading.Timer(15,DHT).start()
	humidity,temp=DHT1.read_retry(11,1)
	print (humidity,'--',temp)
	URL='https://api.thingspeak.com/update?api_key='
	Key='NKPA8X0R8Q5RHSCR'
	HEADER='&field1={}&field2={}'.format(temp,humidity)
	NEW_URL=URL+Key+HEADER
	data=urllib.request.urlopen(NEW_URL)
	print (data)
	time.sleep(10)

if __name__ == '__main__':
	DHT()