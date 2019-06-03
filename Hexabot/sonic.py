#FireHead Ultraschall-Modul
#18.05.2019
#by Fabio Aufinger

import RPi.GPIO as GPIO
import config
import time

def readDistance():
    # Trigger auf "high" setzen (Signal senden) // Copyright Jens Dutzi 2015 / Stand: 12.07.2015
    GPIO.output(config.Trigger, True)
    time.sleep(0.00001)
    # Trigger auf "low" setzen (Signal beenden)
    GPIO.output(config.Trigger, False)
    # Aktuelle Zeit setzen
    StartZeit = time.time()
    StopZeit = StartZeit

    # Warte bis "Echo" auf "low" gesetzt wird und setze danach Start-Zeit erneut
    while GPIO.input(config.Echo) == 0:
        StartZeit = time.time()

    # Warte bis "Echo" auf "high" wechselt (Signal wird empfangen) und setze End-Zeit
    while GPIO.input(config.Echo) == 1:
        StopZeit = time.time()

    # Abstand anhand der Signal-Laufzeit berechnen
    # Schallgeschwindigkeit: 343,50 m/s (bei 20°C Lufttemperatur)
    # Formel: /Signallaufzeit in Sekunden * Schallgeschwindigket in cm/s) / 2 (wg. Hin- und Rückweg des Signals)
    SignalLaufzeit = StopZeit - StartZeit
    dist = round((SignalLaufzeit / 2) * 34350, 2)

    return dist
