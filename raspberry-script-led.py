#!/usr/bin/python
import json
import requests
import time
import RPi.GPIO as GPIO
from snMethod import getserial

f=[]
f.append(4)
f.append(17)
f.append(18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

def cekService(noLED, infoLED, pinGPIO):
  if infoLED == "1":
     print "LED - "+noLED+" hidup"
     GPIO.output(pinGPIO, GPIO.HIGH)
  elif infoLED == "0":
     print "LED - "+noLED+" mati"
     GPIO.output(pinGPIO, GPIO.LOW)

while True:
  #get the feed
  r=requests.get("http://10.10.10.111/raspberry_server/daftar_layanan.php")
  r.text

  #convert it to python dictionary
  data = json.loads(r.text)

  #loop through the result
  i=0
  for item in data:
      cekService(item['LED'], item['INFO'],f[i])
      i=i+1

  time.sleep(1)

GPIO.cleanup()



