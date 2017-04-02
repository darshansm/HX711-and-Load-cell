import RPi.GPIO as gpio
import time

DT =21
SCK=20

HIGH=1
LOW=0

sample=0
val=0

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(SCK, gpio.OUT)
    
def setCursor(x,y):
    if y == 0:
        n=128+x
    elif y == 1:
        n=192+x
    lcdcmd(n)

def readCount():
  i=0
  Count=0
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  while gpio.input(DT) == 1:
      i=0
  for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1

        gpio.output(SCK,0)
        #time.sleep(0.001)
        if gpio.input(DT) == 0: 
            Count=Count+1
            #print Count
        
  gpio.output(SCK,1)
  Count=Count^0x800000
  #time.sleep(0.001)
  gpio.output(SCK,0)
  return Count  

#begin()


time.sleep(3)
sample= readCount()
flag=0
while 1:
    count= readCount()
    w=0
    w=(sample-count)/106
    print w,"g"

  
