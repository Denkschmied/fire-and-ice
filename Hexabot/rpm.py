#FireHead RPM-Modul
#03.06.2019
#by Matteo Hagen
# Ziel: Geschwindigkeit in Drehungen, m/s + rad/s ausgeben.
# Ist für

# Definition Anfangsvariablen (GPIO, Radius Rad):
# ---> Siehe config.py

#Import benötigter Dateien / Bibliotheken
import RPi.GPIO as GPIO
import config as cf
import time
#Start GPIO
GPIO.setup(cf.rpmL, GPIO.IN)
GPIO.setup(cf.rpmR, GPIO.IN)

#Startwert Variablen
RPMcountL = 0 #Zähler seit letztem Reset
RPMcountR = 0 #Zähler seit letztem Reset

totalL = 0 #Gesamtzähler über die gesamte Fahrt
totalR = 0 #Gesamtzähler über die gesamte Fahrt

countL = 0 #Wird nur temporär verwendet
countR = 0 #Wird nur temporär verwendet

##################
### Linkes Rad ###
##################

def t_startL():
    global startL
    startL = start.time()

def t_stopL():
    global stopL
    stopL = stop.time()

def rpmL():

    if countL<=3:
        t_startL()
        countL += 1

    if countL > 3:
        t_stopL()
        RPMcountL += 1
        totalL += 1
        delta = startL - stopL
        radsL = (cf.turns/4)/delta #/4, da die Geschwindigkeit jeweils bei 4 Umdrehungen ausgegeben wird.
        v = (cf.radius_rad*2*pi * radsL)/1000 #Geschwindigkeit in m/s
        return radsL
        return v
        countL = 0

GPIO.add_event_detect(cf.rpmL, GPIO.FALLING, callback=rpmL)

###################
### Rechtes Rad ###
###################

def t_startR():
    global startR
    startR = start.time()

def t_stopR():
    global stopR
    stopR = stop.time()

def rpmR():

    if countR<=3:
        t_startL()
        countL += 1

    if countR > 3:
        t_stopR()
        RPMcountR += 1
        totalR += 1
        delta = start - stop
        radsR = (cf.turns/4)/delta
        v = (cf.radius_rad*2*pi * radsR)/1000 #Geschwindigkeit in m/s
        return radsR
        return v
        countR = 0

GPIO.add_event_detect(cf.rpmR, GPIO.FALLING, callback=rpmR)

def resetcount():
    RPMcountL = 0
    RPMcountR = 0
    return "RPM Counter (L+R) wurden zurückgesetzt."




