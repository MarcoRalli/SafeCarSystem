
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

def prepare(path):

    img = Image.open(path)
    #rgb_im = img.convert('RGB')
    img1 = img.resize(resize_dim, PIL.Image.ANTIALIAS)
    print(img1.size)
    img2 = np.reshape(img1,(1, 300, 200, 3))
    return img2
   

def classification(model, image):

    img_np = prepare(image)
    test = np.array(img_np)
    class_prob=model.predict(test,batch_size=1)
    print(class_prob)
    res = np.where(class_prob == np.max(class_prob))[1]
    print(res)
    if(res == 0):
        return("Safe")
    elif(res == 1 or res == 2 or res == 3 or res == 4 ):
        return("Phone")
    elif(res == 5):
        return("Radio")
    elif(res == 6 or res == 7 or res == 8 or res == 9):
        return("Distraction")



