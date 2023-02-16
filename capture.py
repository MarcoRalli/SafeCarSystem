import cv2
import test
import time


count = 0
num_image = 0
mac_cam = cv2.VideoCapture(0)
while(True):

    retrieve, frames = mac_cam.read()
    cv2.imshow('Try2Catch', frames)
    count = count + 1
    if count == 100:
        cv2.imwrite("image/"+str(num_image)+".jpg",frames)
        count = 0
        num_image = num_image + 1
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break