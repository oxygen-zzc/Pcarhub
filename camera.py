import cv2
import numpy as np

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def return_deviation(self):
        ret,frame = self.cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
        kernel = np.ones((5,5),np.uint8)
        closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
        opening = cv2.morphologyEx(closing,cv2.MORPH_OPEN,kernel)

        line = opening[300]
        black_count = np.sum(line == 0)
        black_index = np.where(line == 0)

        if black_count == 0:
            black_count = 1

        center = (black_index[0][black_count - 1] + black_index[0][0])/2

        deviation = center - 320
        
        return deviation

    def release_cap(self):
        self.cap.release()
