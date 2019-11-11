# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:05:10 2019

@author: System2
"""

import matplotlib.image as pyplot
#from matplotlib.patches import Rectangle
#from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import pandas as pd
import glob
import numpy as np
#import cv2
from PIL import Image
from numpy import asarray

folder = "F:\\Suneel\\face count\\image_data\\"
#filenames = [item for sublist in [glob.glob(folder + ext) for ext in ["/*.png", "/*.jpg", "/*.jfif"]] for item in sublist]
data = pd.read_csv("F:\\Suneel\\face count\\train.csv")
#print(data.head())

#img = "F:\\Suneel\\face count project\\image_data\\10070.jpg"

images = []
#print(filename)
    
#face_cascade = cv2.CascadeClassifier('F:\\Suneel\\face count project\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')

for name in data["Name"]:
    filename = glob.glob(folder+name)
    for img in filename:
        image = Image.open(img)
        detector = MTCNN()
        image = image.convert('RGB')
        pixcel = asarray(image)
        faces = detector.detect_faces(pixcel)
        """image = cv2.imread(img)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage, scaleFactor = 1.001, minNeighbors = 20)"""
        if len(faces) == 0:
            print("No Faces Found")
        else:
            #print(faces)
            #print(faces.shape)
            print("No of Faces: " + str(len(faces)))
        images.append(len(faces))
print(images)
sum1 = np.sum(images)
sum2 = data["HeadCount"].sum()
print((sum1/sum2)*100)
data1 = pd.DataFrame(images)
data1.columns = ["Pred"]
data1["Name"] = data["Name"]
data1["HeadCount"] = data["HeadCount"]
data2 = data1[["Name", "HeadCount","Pred"]]
data2.to_csv("F:\\Suneel\\face count\\final1.csv") 