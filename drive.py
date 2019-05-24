#FireHead Motorantriebs-Modul
#18.05.2019
#by Fabio Aufinger

import RPi.GPIO as GPIO
import config

PWML = GPIO.PWM(config.motorL_PWM, 20)
PWMR = GPIO.PWM(config.motorR_PWM, 20)

def drive(motor, direction, speed):
    PWML.start(0)
    PWMR.start(0)

    if motor == "L" and direction == "F":
        GPIO.output(config.motorL_backward, False)
        GPIO.output(config.motorL_forward, True)
        PWML.ChangeDutyCycle(speed)

    if motor == "L" and direction == "B":
        GPIO.output(config.motorL_forward, False)
        GPIO.output(config.motorL_backward, True)
        PWML.ChangeDutyCycle(speed)

    if motor == "R" and direction == "F":
        GPIO.output(config.motorR_backward, False)
        GPIO.output(config.motorR_forward, True)
        PWMR.ChangeDutyCycle(speed)

    if motor == "R" and direction == "B":
        GPIO.output(config.motorR_forward, False)
        GPIO.output(config.motorR_backward, True)
        PWMR.ChangeDutyCycle(speed)


def stop(motor):
    if motor == "L":
        GPIO.output(config.motorL_backward, False)
        GPIO.output(config.motorL_forward, False)
        PWML.stop()
        
    if motor == "R":
        GPIO.output(config.motorR_backward, False)
        GPIO.output(config.motorR_forward, False)
        PWMR.stop()