
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




if __name__ == "__main__":

    print("System is going to start----->\n")
    vgg_model_dropout = None
    #while(vgg_model_dropout != None):
    print(".......\n")
    flag = 0
    count = 0
    vgg_model = tf.keras.models.load_model("mode/CNN_pretrained/CNN_VGG16_Dropout_fineTuning2/model.h5")
  
    for image in os.listdir("phone"):
        print(classification.classification(vgg_model, "phone/"+image))
       
        # if res != 0:
        #     count = count +1
        #     if count == 2:
        #         flag = 1
        # print(flag)
 
