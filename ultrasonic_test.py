from ultrasonic import Ultrasonic
import time
import RPi.GPIO as GPIO

try:
    ul = Ultrasonic()
    while True:
        print(str(ul.left_distance())+'cm   '+str(ul.right_distance())+'cm')
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()


