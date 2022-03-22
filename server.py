import RPi.GPIO as GPIO
import time
from car import Car
from avoid import Avoid
from track import Track
import LCD1602
import os
from bottle import route,run,template,request,static_file
import bottle
import sys
import signal
import threading
from camera import Camera
from ultrasonic import Ultrasonic

car = Car()
car.reset()
camera = Camera()
ul = Ultrasonic()

LCD1602.init(0x27,1)
LCD1602.write(0,0,'     Pcarhub    ')
time.sleep(2)

isAuto = False

# def auto_drive():
#     track = Track()
#     while True:
#         if isAuto is True:
#             l = track.track_left()
#             r = track.track_right()
#             if l==0 and r==0:
#                 car.reset()
#             elif l==1 and r==0:
#                 car.full_left()
#             elif l==0 and r==1:
#                 car.full_right()
#             elif l==1 and r==1:
#                 car.full_forward()
#             time.sleep(0.1)

def auto_drive():
    while True:
        if isAuto = True:
            deviation = camera.return_deviation()
            dis_left = ul.left_distance()
            dis_right = ul.right_distance()

            print(deviation)
            # if deviation <= 20 and deviation >= -20:
            #     car.full_forward()
            # elif deviation > 20:
            #     car.right_stop()
            # elif deviation < -20:
            #     car.left_stop()

            if deviation <= 20 and deviation >= -20 and dis_left < 8:
                car.right_stop()
            elif deviation <= 20 and deviation >= -20 and dis_right < 8:
                car.left_stop()
            elif deviation <= 20 and deviation >= -20:
                car.full_forward()
            elif deviation < -20 and dis_left < 8:
                car.right_stop()
            elif deviation < -20 and dis_right < 8:
                car.left_stop()
            elif deviation < -20:
                car.left_stop()
            elif deviation > 20 and dis_left < 8:
                car.right_stop()
            elif deviation > 20 and dis_right < 8:
                car.left_stop()
            elif deviation > 20:
                car.right_stop()

bottle.TEMPLATE_PATH.append('/media/zczhang/32F09614F095DF03/Raspberry Pi/Pcarhub-code/Pcar')
@route('/')
def index():
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    # return template(currentPath+r'/index.html')
    return template('index.html')

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root='/media/zczhang/32F09614F095DF03/Raspberry Pi/Pcarhub-code/Pcar/static')

@route('/operate',method='POST')
def operate():
    global isRun
    global isAuto
    parameter = request.forms.get('parameter')
    print(parameter)
    if parameter == 'forward':
        car.full_forward()
    elif parameter == 'back':
        car.full_back()
    elif parameter == 'left':
        car.full_left()
    elif parameter == 'right':
        car.full_right()
    elif parameter == 'stop':
        car.reset()
    elif parameter == 'rleft':
        car.full_left()
    elif parameter == 'rright':
        car.full_right()
    elif parameter == 'auto':
        isAuto = True
        thread_auto = threading.Thread(target=auto_drive)
        thread_auto.start()
    elif parameter == 'autostop':
        isAuto = False

@route('/display',method='POST')
def display():
    parameter = request.forms.get('parameter')
    print(parameter[0:16])
    print(parameter[16:32])
    # LCD1602.init(0x27,1)
    # LCD1602.write(0,0,parameter[0:16])
    # LCD1602.write(0,1,parameter[16:32])
    # time.sleep(2)

def exit(signum,frame):
    print('Exit')
    GPIO.cleanup()
    camera.release_cap()
    sys.exit(0)

run(host='localhost',port=8081)

signal.signal(signal.SIGINT,exit)
signal.signal(signal.SIGTERM,exit)

while True:
    pass




