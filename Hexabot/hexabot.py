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

while true:
    d.drive(L,F, 30)
    print(s.readDistance(cf.EchoL,cf.TriggerL))

#
# ### Startposition ###
# X = 0
# Y = 0
# dirX = 0
#
#
# ### Start ###
# #Press s to Start
# print("s to start, e to exit, r to return (only after start)")
#
# try:
#  	while True: # create an infinte loop to keep the script running
#  	 	time.sleep(0.1)
#
# while(1):
#     x = raw_input()
#     if x == 's':
#
#         distL =
#
#     if x == 'r':
#         if
#             else
#
# except KeyboardInterrupt:
#     pass
#
# finally:
#     c.stop()
#     GPIO.cleanup()
