
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


import classification

if __name__ == "__main__":

    print("System is going to start----->\n")
    vgg_model_dropout = None
    while(vgg_model_dropout != None):
        print(".......\n")
        vgg_model_dropout = tf.keras.models.load_model("model/CNN_VGG16_Dropout_fineTuning2/model.h5")
       
    print("Image capturing system online")
    #arrivo dell'immagige e processazione

    
    classification.classification(vgg_model_dropout, image)
