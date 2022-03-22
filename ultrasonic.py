import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.l_trig = 18
        self.l_echo = 23

        self.r_trig = 12
        self.r_echo = 16

        GPIO.setup(self.l_trig,GPIO.OUT)
        GPIO.setup(self.l_echo,GPIO.IN)

        GPIO.setup(self.r_trig,GPIO.OUT)
        GPIO.setup(self.r_echo,GPIO.IN)

    def left_distance(self):
        GPIO.output(self.l_trig,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.l_trig,GPIO.LOW)

        while GPIO.input(self.l_echo) == 0:
            pass
        t1 = time.time()

        while GPIO.input(self.l_echo) == 1:
            pass
        t2 = time.time()

        t3 = t2 - t1
        
        return t3 * 340 / 2 * 100

    def right_distance(self):
        GPIO.output(self.r_trig,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.r_trig,GPIO.LOW)

        while GPIO.input(self.r_echo) == 0:
            pass
        t1 = time.time()

        while GPIO.input(self.r_echo) == 1:
            pass
        t2 = time.time()

        t3 = t2 - t1
        
        return t3 * 340 / 2 * 100