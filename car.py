import RPi.GPIO as GPIO
import time
import pigpio

class Car:
    def __init__(self):
        self.FIA = 20
        self.FI1 = 6
        self.FI2 = 13
        self.FI3 = 19
        self.FI4 = 26
        self.FIB = 21

        self.BIA = 24
        self.BI1 = 17
        self.BI2 = 27
        self.BI3 = 25
        self.BI4 = 22
        self.BIB = 5

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.FIA,GPIO.OUT)
        GPIO.setup(self.FI1,GPIO.OUT)
        GPIO.setup(self.FI2,GPIO.OUT)
        GPIO.setup(self.FI3,GPIO.OUT)
        GPIO.setup(self.FI4,GPIO.OUT)
        GPIO.setup(self.FIB,GPIO.OUT)

        GPIO.setup(self.BIA,GPIO.OUT)
        GPIO.setup(self.BI1,GPIO.OUT)
        GPIO.setup(self.BI2,GPIO.OUT)
        GPIO.setup(self.BI3,GPIO.OUT)
        GPIO.setup(self.BI4,GPIO.OUT)
        GPIO.setup(self.BIB,GPIO.OUT)

        self.pi = pigpio.pi()

    def reset(self):
        GPIO.output(self.FIA,GPIO.LOW)
        GPIO.output(self.FI1,GPIO.LOW)
        GPIO.output(self.FI2,GPIO.LOW)
        GPIO.output(self.FI3,GPIO.LOW)
        GPIO.output(self.FI4,GPIO.LOW)
        GPIO.output(self.FIB,GPIO.LOW)

        GPIO.output(self.BIA,GPIO.LOW)
        GPIO.output(self.BI1,GPIO.LOW)
        GPIO.output(self.BI2,GPIO.LOW)
        GPIO.output(self.BI3,GPIO.LOW)
        GPIO.output(self.BI4,GPIO.LOW)
        GPIO.output(self.BIB,GPIO.LOW)

    def set_speed(self,channel,x):
        self.pi.write(channel,1)
        self.pi.set_PWM_frequency(channel,50)
        self.pi.set_PWM_range(channel,1000)
        self.pi.set_PWM_dutycycle(channel,x)

    def top_left_forward(self,x):
        GPIO.output(self.FI1,GPIO.HIGH)
        GPIO.output(self.FI2,GPIO.LOW)
        self.set_speed(self.FIA,x)

    def top_left_back(self,x):
        GPIO.output(self.FI1,GPIO.LOW)
        GPIO.output(self.FI2,GPIO.HIGH)
        self.set_speed(self.FIA,x)

    def top_right_forward(self,x):
        GPIO.output(self.FI3,GPIO.HIGH)
        GPIO.output(self.FI4,GPIO.LOW)
        self.set_speed(self.FIB,x)

    def top_right_back(self,x):
        GPIO.output(self.FI3,GPIO.LOW)
        GPIO.output(self.FI4,GPIO.HIGH)
        self.set_speed(self.FIB,x)

    def bottom_left_forward(self,x):
        GPIO.output(self.BI1,GPIO.HIGH)
        GPIO.output(self.BI2,GPIO.LOW)
        self.set_speed(self.BIA,x)
    
    def bottom_left_back(self,x):
        GPIO.output(self.BI1,GPIO.LOW)
        GPIO.output(self.BI2,GPIO.HIGH)
        self.set_speed(self.BIA,x)

    def bottom_right_forward(self,x):
        GPIO.output(self.BI3,GPIO.HIGH)
        GPIO.output(self.BI4,GPIO.LOW)
        self.set_speed(self.BIB,x)

    def bottom_right_back(self,x):
        GPIO.output(self.BI3,GPIO.LOW)
        GPIO.output(self.BI4,GPIO.HIGH)
        self.set_speed(self.BIB,x)

    def forward(self,x):
        self.reset()
        self.top_left_forward(x)
        self.top_right_forward(x)
        self.bottom_left_forward(x)
        self.bottom_right_forward(x)

    def back(self,x):
        self.reset()
        self.top_left_back(x)
        self.top_right_back(x)
        self.bottom_left_back(x)
        self.bottom_right_back(x)

    def left(self,x):
        self.reset()
        self.top_right_forward(x)
        self.bottom_right_forward(x)

    def right(self,x):
        self.reset()
        self.top_left_forward(x)
        self.bottom_left_forward(x)

    def turn_left(self):
        GPIO.output(self.FI1,GPIO.LOW)
        GPIO.output(self.FI2,GPIO.LOW)
        GPIO.output(self.BI1,GPIO.LOW)
        GPIO.output(self.BI2,GPIO.LOW)

    def turn_right(self):
        GPIO.output(self.FI3,GPIO.LOW)
        GPIO.output(self.FI4,GPIO.LOW)
        GPIO.output(self.BI3,GPIO.LOW)
        GPIO.output(self.BI4,GPIO.LOW)

    def roll_left(self,x):
        self.reset()
        self.top_left_back(x)
        self.bottom_left_back(x)
        self.top_right_forward(x)
        self.bottom_right_forward(x)

    def roll_right(self,x):
        self.reset()
        self.top_left_forward(x)
        self.bottom_left_forward(x)
        self.top_right_back(x)
        self.bottom_right_back(x)

    def clean(self):
        GPIO.cleanup()



    def full_top_left_forward(self):
        GPIO.output(self.FI1,GPIO.HIGH)
        GPIO.output(self.FI2,GPIO.LOW)
        GPIO.output(self.FIA,GPIO.HIGH)

    def full_top_left_back(self):
        GPIO.output(self.FI1,GPIO.LOW)
        GPIO.output(self.FI2,GPIO.HIGH)
        GPIO.output(self.FIA,GPIO.HIGH)
    
    def full_top_right_forward(self):
        GPIO.output(self.FI3,GPIO.HIGH)
        GPIO.output(self.FI4,GPIO.LOW)
        GPIO.output(self.FIB,GPIO.HIGH)

    def full_top_right_back(self):
        GPIO.output(self.FI3,GPIO.LOW)
        GPIO.output(self.FI4,GPIO.HIGH)
        GPIO.output(self.FIB,GPIO.HIGH)

    def full_bottom_left_forward(self):
        GPIO.output(self.BI1,GPIO.HIGH)
        GPIO.output(self.BI2,GPIO.LOW)
        GPIO.output(self.BIA,GPIO.HIGH)

    def full_bottom_left_back(self):
        GPIO.output(self.BI1,GPIO.LOW)
        GPIO.output(self.BI2,GPIO.HIGH)
        GPIO.output(self.BIA,GPIO.HIGH)

    def full_bottom_right_forward(self):
        GPIO.output(self.BI3,GPIO.HIGH)
        GPIO.output(self.BI4,GPIO.LOW)
        GPIO.output(self.BIB,GPIO.HIGH)

    def full_bottom_right_back(self):
        GPIO.output(self.BI3,GPIO.LOW)
        GPIO.output(self.BI4,GPIO.HIGH)
        GPIO.output(self.BIB,GPIO.HIGH)


    def full_forward(self):
        self.reset()
        self.full_top_left_forward()
        self.full_top_right_forward()
        self.full_bottom_left_forward()
        self.full_bottom_right_forward()

    def full_back(self):
        self.reset()
        self.full_top_left_back()
        self.full_top_right_back()
        self.full_bottom_left_back()
        self.full_bottom_right_back()

    def full_left(self):
        self.reset()
        self.full_top_right_forward()
        self.full_bottom_right_forward()

    def full_right(self):
        self.reset()
        self.full_top_left_forward()
        self.full_bottom_left_forward()

    def left_stop(self):
        # GPIO.output(self.FI1,GPIO.LOW)
        # GPIO.output(self.FI2,GPIO.LOW)
        # GPIO.output(self.BI1,GPIO.LOW)
        # GPIO.output(self.BI2,GPIO.LOW)
        GPIO.output(self.FIA,GPIO.LOW)
        GPIO.output(self.BIA,GPIO.LOW)
        GPIO.output(self.FIB,GPIO.HIGH)
        GPIO.output(self.BIB,GPIO.HIGH)

    def right_stop(self):
        GPIO.output(self.FIB,GPIO.LOW)
        GPIO.output(self.BIB,GPIO.LOW)
        GPIO.output(self.FIA,GPIO.HIGH)
        GPIO.output(self.BIA,GPIO.HIGH)

    