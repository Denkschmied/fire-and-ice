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