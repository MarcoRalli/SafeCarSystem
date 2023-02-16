
import numpy as np
import random as rn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import VGG16
import PIL
from PIL import Image
import cv2
import os
import classification
from playsound import playsound


if __name__ == "__main__":

    count = 0
    num_image = 0
    flag_safe = 0
    flag_dist = 0
    flag_phone = 0

    print("System is going to start----->\n")
    

    print(".......\n")

    mac_cam = cv2.VideoCapture(0)
    vgg_model = tf.keras.models.load_model("mode/CNN_pretrained/CNN_VGG16_Dropout_fineTuning2/model.h5")

    while(True):

        retrieve, frames = mac_cam.read()
        cv2.imshow('Try2Catch', frames)
        count = count + 1
        if count == 20:
            
            cv2.imwrite("image/"+str(num_image)+".png",frames)
            count = 0
            num_image = num_image + 1

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        if len(os.listdir("image")) == 10:
            for image in os.listdir("image"):
                if classification.classification(vgg_model,"image/"+image) == "Phone":
                   flag_phone = flag_phone + 1
                elif classification.classification(vgg_model,"image/"+image) == "Distraction":
                    flag_dist = flag_dist + 1
                else:
                    flag_safe = flag_safe + 1
                os.remove("image/"+image)
                num_image = 0
     
            if max(flag_phone, flag_dist, flag_safe) == flag_dist:
                playsound('audio/dist.m4a')
            elif max(flag_phone, flag_dist, flag_safe) == flag_phone:
                playsound('audio/phone.m4a')
            elif max(flag_phone, flag_dist, flag_safe) == flag_safe:
                playsound('audio/safe.m4a')

            flag_safe = 0
            flag_phone = 0
            flag_dist = 0
    
 