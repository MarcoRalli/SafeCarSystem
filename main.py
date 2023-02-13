
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



resize_dim = (300, 200)


if __name__ == "__main__":

    print("System is going to start----->\n")
    vgg_model_dropout = None
    #while(vgg_model_dropout != None):
    print(".......\n")
    image = tf.keras.utils.load_img("dis1.PNG", target_size = resize_dim )
    input_arr = tf.keras.utils.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.

    vgg_model_dropout = tf.keras.models.load_model("model/CNN_pretrained/CNN_VGG16_Dropout_fineTuning/model.h5")
    class_prob=vgg_model_dropout.predict(input_arr,batch_size=1)
    print(class_prob)

        
        
       

    
    #print(classification.classification(vgg_model_dropout, "data_to_test/c1/img_520.jpg"))
