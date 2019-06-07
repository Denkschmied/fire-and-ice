#rpmreader v2
# by mausausdruck1. 06.06.19
#
#teilweise angelehnt auf dem Code von
#FireHead RPM-Modul
#03.06.2019
#by Matteo Hagen


### USAGE

# 1. Setup conf
# 2. include modules + rpminit()
# 3. get you RPM via rpmread.rpm as list (left, right) 
# 4. if you change your drive direction call rpmread.resetL() or rpmread.resetR()

# (un) commend gpio Setmode in some case!

###


import RPi.GPIO as GPIO
import config as cf
import time
import sys

counterL=0
timerL=0
timerR=0
counterR=0

rpm=[0,0] #rpm L/R

def rpminit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cf.rpmL, GPIO.IN) 
    GPIO.add_event_detect(cf.rpmL, GPIO.FALLING, callback=countL)    
    GPIO.setup(cf.rpmR, GPIO.IN) 
    GPIO.add_event_detect(cf.rpmR, GPIO.FALLING, callback=countR)
    
def getTime():
    if sys.version_info < (3,7,0):
        return time.time()
    else:
        return time.time_ns() / (10 ** 9) # genauere Zeit ab 3.7 in s float
    

def countL(var):
    global counterL, rpm, timerL
    
    if timerL==0:## init
        timerL=getTime()       
        
    if counterL >= 2:
        dt=getTime()-timerL
        ds=counterL/cf.Drehscheibe
        rpm[0]+=ds/dt * 60 # U pro Minute
        counterL=0
        timerL=getTime()
    else:        
        counterL=counterL+1
    
def resetL():
    global rpm, timerL, counterL
    rpm[0]=0;
    timerL=0;
    counterL=0;

def countR(var):
    global counterR, rpm, timerR
    
    if timerR==0:## init
        timerR=getTime()       
        
    if counterR >= 2:
        dt=getTime()-timerR
        ds=counterR/cf.Drehscheibe
        rpm[1]+=ds/dt * 60 # U pro Minute
        counterR=0
        timerR=getTime()
    else:        
        counterR=counterR+1
    
def resetR():
    global rpm, timerR, counterR
    rpm[1]=0;
    timerR=0;
    counterR=0;
    

# Test

#while True:
   # print(rpm)
