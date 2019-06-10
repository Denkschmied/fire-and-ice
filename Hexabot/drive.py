#FireHead Motorantriebs-Modul
#18.05.2019
#by Fabio Aufinger

import RPi.GPIO as GPIO
import config

PWML = GPIO.PWM(config.motorL_PWM, 20)
PWMR = GPIO.PWM(config.motorR_PWM, 20)

def drive(directionL, directionR, speedL, speedR):
    PWML.start(0)
    PWMR.start(0)

    if directionL == "F" and directionR == "F":
        GPIO.output(config.motorL_backward, False)
        GPIO.output(config.motorL_forward, True)
        GPIO.output(config.motorR_backward, False)
        GPIO.output(config.motorR_forward, True)
        PWML.ChangeDutyCycle(speedL)
        PWMR.ChangeDutyCycle(speedR)

    if directionL == "F" and directionR == "B":
        GPIO.output(config.motorL_forward, True)
        GPIO.output(config.motorL_backward, False)
        GPIO.output(config.motorR_forward, False)
        GPIO.output(config.motorR_backward, True)
        PWML.ChangeDutyCycle(speedL)
        PWMR.ChangeDutyCycle(speedR)

    if directionL == "B" and directionR == "B":
        GPIO.output(config.motorL_forward, False)
        GPIO.output(config.motorL_backward, True)
        GPIO.output(config.motorR_forward, False)
        GPIO.output(config.motorR_backward, True)
        PWML.ChangeDutyCycle(speedL)
        PWMR.ChangeDutyCycle(speedR)

    if directionL == "B" and directionR == "F":
        GPIO.output(config.motorL_forward, False)
        GPIO.output(config.motorL_backward, True)
        GPIO.output(config.motorR_forward, True)
        GPIO.output(config.motorR_backward, False)
        PWML.ChangeDutyCycle(speedL)
        PWMR.ChangeDutyCycle(speedR)

def stop(motor):
    if motor == "L":
        GPIO.output(config.motorL_backward, False)
        GPIO.output(config.motorL_forward, False)
        PWML.stop()
        
    if motor == "R":
        GPIO.output(config.motorR_backward, False)
        GPIO.output(config.motorR_forward, False)
        PWMR.stop()
