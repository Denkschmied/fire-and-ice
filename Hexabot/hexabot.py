### Start/Stop
###
###
###
###
###
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import config as cf
#### GPIO setup PINs ###
# Motor
GPIO.setup(cf.motorL_PWM, GPIO.OUT)
GPIO.setup(cf.motorL_forward, GPIO.OUT)
GPIO.setup(cf.motorL_backward, GPIO.OUT)

GPIO.setup(cf.motorR_PWM, GPIO.OUT)
GPIO.setup(cf.motorR_forward, GPIO.OUT)
GPIO.setup(cf.motorR_backward, GPIO.OUT)

import drive as d
import sonic as s
import rpm as r
#import gyro as g

# Ultraschall
GPIO.setup(cf.TriggerL, GPIO.OUT)
GPIO.setup(cf.EchoL, GPIO.IN)
GPIO.setup(cf.TriggerM, GPIO.OUT)
GPIO.setup(cf.EchoM, GPIO.IN)
GPIO.setup(cf.TriggerR, GPIO.OUT)
GPIO.setup(cf.EchoR, GPIO.IN)

# RPM
GPIO.setup(cf.rpmL, GPIO.IN)
GPIO.setup(cf.rpmR, GPIO.IN)

# FLAME
GPIO.setup(cf.flame_input, GPIO.IN)

speed = 5 #Umdrehungen pro Sekunde
PWML = 0
PWMR = 0

while True:
    deltavL = speed - r.rpmL()
    deltavR = speed - r.rpmR()
    PWML = PWML + deltavL
    PWMR = PWMR + deltavR

    #if s.readDistance(cf.EchoM, cf.TriggerL) < 30 and s.readDistance(cf.EchoM, cf.TriggerL) > 20:
        #speed = speed - 30
    #if s.readDistance(cf.EchoM, cf.TriggerL) < 20 and s.readDistance(cf.EchoM, cf.TriggerL) > 10:
        #speed = speed - 50
    print("s to start, e to exit, a to abort, r to return (only after start)")
    x = raw_input()
    if x == 's':
        d.drive("B", "F", PWML, PWMR)
    if x == 'a':
        d.stop("L")
        d.stop("R")
    if x == 'e':
        d.stop("L")
        d.stop("R")
        GPIO.cleanup()
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
