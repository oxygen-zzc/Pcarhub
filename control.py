import threading
from tkinter import *
import time
import sys
from car import Car
from avoid import Avoid

all_speed = 200
car = Car()
avoid = Avoid()
is_forward = False

def forward():
    car.forward(all_speed)

def back():
    car.back(all_speed)

def left():
    car.left(all_speed)

def right():
    car.right(all_speed)

def stop():
    global is_forward
    car.stop()
    is_forward = False

def start():
    global is_forward
    car.forward(all_speed)
    is_forward = True

def roll_left():
    car.roll_left(all_speed)

def roll_right():
    car.roll_right(all_speed)

def exit():
    car.clean()
    sys.exit(0)

def gui():
    root = Tk()
    root.title('RUN')
    root.geometry('400x400')
    btn1 = Button(root, text='前进', command=forward)
    btn1.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.3)
    btn2 = Button(root, text='后退', command=back)
    btn2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.3)
    btn3 = Button(root, text='左转', command=left)
    btn3.place(relx=0.02, rely=0.35, relwidth=0.3, relheight=0.3)
    btn4 = Button(root, text='右转', command=right)
    btn4.place(relx=0.68, rely=0.35, relwidth=0.3, relheight=0.3)
    btn5 = Button(root, text='左旋', command=roll_left)
    btn5.place(relx=0.02, rely=0.02, relwidth=0.3, relheight=0.3)
    btn6 = Button(root, text='右旋', command=roll_right)
    btn6.place(relx=0.68, rely=0.02, relwidth=0.3, relheight=0.3)
    btn7 = Button(root, text='停止', command=stop)
    btn7.place(relx=0.35, rely=0.68, relwidth=0.3, relheight=0.3)
    btn8 = Button(root, text='结束', command=exit)
    btn8.place(relx=0.02, rely=0.68, relwidth=0.3, relheight=0.3)
    btn9 = Button(root, text='开始', command=start)
    btn9.place(relx=0.68, rely=0.68, relwidth=0.3, relheight=0.3)
    root.mainloop()

def ir_turn():
    while True:
        if is_forward is True:
            l = avoid.left_result()
            r = avoid.right_result()
            if l==0 and r==0:
                car.stop()
            elif l==0 and r==1:
                car.right(all_speed)
            elif l==1 and r==0:
                car.left(all_speed)
            elif l==1 and r==1:
                car.forward(all_speed)

if __name__=='__main__':
    t_gui = threading.Thread(target=gui)
    t_gui.start()

    t_turn = threading.Thread(target=ir_turn)
    t_turn.start()