import RPi.GPIO as GPIO
import config
import time

steps = 0
steps_old = 0
start_time = 0
end_time = 0

def read_RPM_L():


    return steps



def read_RPM_R():


##############################
#Python Code Hall-Sensor
##############################
# !/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import time, math

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
sensor = 12
pulse = 0
start_timer = time.time()

def init_GPIO():  # initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)

def calculate_elapse(channel):  # callback function
    global pulse, start_timer, elapse
    pulse += 1  # increase pulse by 1 whenever interrupt occurred
    elapse = time.time() - start_timer  # elapse for every 1 complete rotation made!
    start_timer = time.time()  # let current time equals to start_timer

def calculate_speed(r_cm):
    global pulse, elapse, rpm, dist_km, dist_meas, km_per_sec, km_per_hour
    if elapse != 0:  # to avoid DivisionByZero error
        rpm = 1 / elapse * 60
        circ_cm = (2 * math.pi) * r_cm  # calculate wheel circumference in CM
        dist_km = circ_cm / 100000  # convert cm to km
        km_per_sec = dist_km / elapse  # calculate KM/sec
        km_per_hour = km_per_sec * 3600  # calculate KM/h
        dist_meas = (dist_km * pulse) * 1000  # measure distance traverse in meter
        return km_per_hour

def init_interrupt():
    GPIO.add_event_detect(sensor, GPIO.FALLING, callback=calculate_elapse, bouncetime=20)

if __name__ == '__main__':
    init_GPIO()
    init_interrupt()
    while True:
        calculate_speed(20)  # call this function with wheel radius as parameter
        print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(rpm, km_per_hour, dist_meas,
                                                                                    pulse))
        sleep(0.1)





########################
#Arudino Code 1
########################

int encoder_pin = 2; // pulse output from the module
unsigned int rpm; // rpm reading
volatile byte pulses; // number of pulses
unsigned long timeold;
// number of pulses per revolution
// based on your encoder disc
unsigned int pulsesperturn = 12;
void counter()
{
   //Update count
   pulses++;
}
void setup()
{
   Serial.begin(9600);
   pinMode(encoder_pin, INPUT);
   //Interrupt 0 is digital pin 2
   //Triggers on Falling Edge (change from HIGH to LOW)
   attachInterrupt(0, counter, FALLING);
   // Initialize
   pulses = 0;
   rpm = 0;
   timeold = 0;
}
void loop()
{
   if (millis() - timeold >= 1000) {
      //Don't process interrupts during calculations
      detachInterrupt(0);
      rpm = (60 * 1000 / pulsesperturn )/ (millis() - timeold)* pulses;
      timeold = millis();
      pulses = 0;
      Serial.print("RPM = ");
      Serial.println(rpm,DEC);
      //Restart the interrupt processing
      attachInterrupt(0, counter, FALLING);
   }
}


##########################################
#Arduino Code 2
##########################################

    start_time = millis();
end_time = start_time + 1000;
while (millis() < end_time)
    {
    if (digitalRead(sensor))
    {
        steps = steps + 1;
    while (digitalRead(sensor));
    }
    lcd.setCursor(9, 0);

    temp = steps - steps_old;
    steps_old = steps;
    rps = (temp / 20);
