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
import server_tcp
from playsound import playsound


if __name__ == "__main__":

    count = 0
    num_image = 0
    flag_safe = 0
    flag_dist = 0
    flag_phone = 0

    print("System is going to start----->\n")
    

    print(".......\n")
    dest_folder = 'image/'
    
    vgg_model = tf.keras.models.load_model('model/model.h5')

    while(True):

        path_img = server_tcp.get_raspberry_image(dest_folder)
        img = cv2.imread(path_img)
        cv2.imshow('output',img)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        if len(os.listdir("image")) == 5:
            for image in os.listdir("image"):
                result = classification.classification(vgg_model,"image/"+image)
                print("Result: " + result)
                if  result == "Phone":
                   flag_phone = flag_phone + 1
                elif result == "Distraction":
                    flag_dist = flag_dist + 1
                else:
                    flag_safe = flag_safe + 1
                os.remove("image/"+image)
                num_image = 0
     
            if max(flag_phone, flag_dist, flag_safe) == flag_dist:
                playsound('audio/dist.mp3')
            elif max(flag_phone, flag_dist, flag_safe) == flag_phone:
                playsound('audio/phone.mp3')
            elif max(flag_phone, flag_dist, flag_safe) == flag_safe:
                playsound('audio/safe.mp3')

            flag_safe = 0
            flag_phone = 0
            flag_dist = 0
    
 
