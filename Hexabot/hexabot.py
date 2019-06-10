##################################
#INIT
##################################

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import config as cf
#### GPIO setup PINs und Import Module ###
# Motor
GPIO.setup(cf.motorL_PWM, GPIO.OUT)
GPIO.setup(cf.motorL_forward, GPIO.OUT)
GPIO.setup(cf.motorL_backward, GPIO.OUT)

GPIO.setup(cf.motorR_PWM, GPIO.OUT)
GPIO.setup(cf.motorR_forward, GPIO.OUT)
GPIO.setup(cf.motorR_backward, GPIO.OUT)
import drive as d

# RPM
import rpm as r
r.rpminit()

# LED
import led

# Ultraschall
GPIO.setup(cf.TriggerL, GPIO.OUT)
GPIO.setup(cf.EchoL, GPIO.IN)
GPIO.setup(cf.TriggerM, GPIO.OUT)
GPIO.setup(cf.EchoM, GPIO.IN)
GPIO.setup(cf.TriggerR, GPIO.OUT)
GPIO.setup(cf.EchoR, GPIO.IN)
import sonic as s

# FLAME
GPIO.setup(cf.flame_input, GPIO.IN)

# Multithread
from _thread import start_new_thread

start_new_thread(led.LED, ())

##################################
#VAR
##################################
speed = 100.0 #Umdrehungen pro Sekunde
PWML = 1.0
PWMR = 1.0

##################################
#MAIN
##################################

while True:
    deltavL = speed - r.rpm[0]

    if deltavL >= 0:
        PWML = PWML + 0.5
        if PWML > 100:
            PWML = PWML - 0.5
    elif deltavL < 0:
        PWML = PWML - 0.5
        if PWML < 0:
            PWML = PWML + 0.5

            
    deltavR = speed - r.rpm[1]

    if deltavR < 0:
        PWMR = PWMR - 0.5
        if PWMR > 100:
            PWMR = PWMR - 0.5
    elif deltavR >= 0:
        PWMR = PWMR + 0.5
        if PWMR < 0:
            PWMR = PWMR + 0.5
            
    d.drive("F", "F", PWML, PWMR)

    print(r.rpm, end='\r')
    print("deltavL:",deltavL, end='\r')
    print("PWML:",PWML, end='\r')
    print("deltavR:",deltavR, end='\r')
    print("PWMR:", PWMR, end='\r')

    



    #if s.readDistance(cf.EchoM, cf.TriggerL) < 30 and s.readDistance(cf.EchoM, cf.TriggerL) > 20:
        #speed = speed - 30
    #if s.readDistance(cf.EchoM, cf.TriggerL) < 20 and s.readDistance(cf.EchoM, cf.TriggerL) > 10:
        #speed = speed - 50
##    print("s to start, e to exit, a to abort, r to return (only after start)")
##    x = raw_input()
##    if x == 's':
##        d.drive("B", "F", 50, 50)
##    if x == 'a':
##        d.stop("L")
##        d.stop("R")
##    if x == 'e':
##        d.stop("L")
##        d.stop("R")
##        GPIO.cleanup()
    # except KeyboardInterrupt:
    #     c.stop()
    #     GPIO.cleanup()
    #     raise Exception, "Ende"



# finally:
#     d.stop("L")
#     d.stop("R")
#     GPIO.cleanup()
#
# ### Startposition ###
# X = 0
# Y = 0
# dirX = 0
#
