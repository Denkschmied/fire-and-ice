### Start/Stop
###
###
###
###
###
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import config as cf
import drive as d
import sonic as s
#import gyro as g

#### GPIO setup PINs ###
# Motor
GPIO.setup(cf.motorL_PWM, GPIO.OUT)
GPIO.setup(cf.motorL_forward, GPIO.OUT)
GPIO.setup(cf.motorL_backward, GPIO.OUT)

GPIO.setup(cf.motorR_PWM, GPIO.OUT)
GPIO.setup(cf.motorR_forward, GPIO.OUT)
GPIO.setup(cf.motorR_backward, GPIO.OUT)

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
print("s to start, e to exit, r to return (only after start)")
while True:
    # Press s to Start
    try:
        x = raw_input()
        if x == 's':
            d.drive("L", "F", 10)
            d.drive("R", "F", 10)
            print(s.readDistance(cf.EchoL, cf.TriggerL))
        if x == 'r':
            d.stop("L")
            d.stop("R")
    #
    # except KeyboardInterrupt:
    #     c.stop()
    #     GPIO.cleanup()
    #     raise Exception, "Ende"

#
# ### Startposition ###
# X = 0
# Y = 0
# dirX = 0
#
