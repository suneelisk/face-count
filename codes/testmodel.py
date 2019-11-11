# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:03:05 2019

@author: System2
"""

import pandas as pd
import glob
import cv2

folder = "F:\\suneel\\face count\\image_data\\"
#filenames = [item for sublist in [glob.glob(folder + ext) for ext in ["/*.png", "/*.jpg", "/*.jfif"]] for item in sublist]
data = pd.read_csv("F:\\suneel\\face count\\test_Rj9YEaI.csv")
#print(data.head())

images = []
    #print(filename)
    
face_cascade = cv2.CascadeClassifier('F:\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')

for name in data["Name"]:
    filename = glob.glob(folder+name)
    for img in filename:
        image = cv2.imread(img)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage)
        if len(faces) == 0:
            print("No Faces Found")
        else:
            #print(faces)
            #print(faces.shape)
            print("No of Faces: " + str(faces.shape[0]))
            images.append(faces.shape[0])
            
data1 = pd.DataFrame(images)
data1.columns = ["Count"]
data1["Name"] = data["Name"]
data2 = data1[["Name", "Count"]]
data2.to_csv("F:\\suneel\\face count\\final.csv")           
