import time
from RailSwitch import *

SW1_PIN = 14
SW2_PIN = 15
LED_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
sw1 = RailSwitch(SW1_PIN)
sw2 = RailSwitch(SW2_PIN)

try:
    while(True):
        if (sw1.is_pushed()):
            GPIO.output(LED_PIN, GPIO.HIGH)
        if (sw2.is_pushed()):
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("break")
    GPIO.cleanup()

