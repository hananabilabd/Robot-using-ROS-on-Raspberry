import wiringpi
import time
wiringpi.wiringPiSetup()
wiringpi.pinMode(1,1)
while True:
    time.sleep(0.5)
    wiringpi.digitalWrite(1,1)
    time.sleep(0.5)
    wiringpi.digitalWrite(1,0)
