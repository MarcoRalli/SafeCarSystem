
import os
import shutil
import numpy as np
import random as rn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import VGG16
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import f1_score
import PIL
from PIL import Image
     
import cv2


resize_dim = (300, 200)

   

def classification(model, image):

    img = tf.keras.utils.load_img(image, target_size = resize_dim, interpolation = "bilinear")
    input_arr = tf.keras.utils.img_to_array(img)
    input_arr = np.array([input_arr])  # Convert single image to a batch.

    class_prob=model.predict(input_arr,batch_size=1)

    res = np.where(class_prob == np.max(class_prob))[1]
    if(res == 0):
        return("Phone")
    elif(res == 1 ):
        return("Distraction")
    elif(res == 2):
        return("Safe")
 
 


