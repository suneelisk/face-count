# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:03:05 2019

@author: System2
"""
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import pandas as pd
import glob
#import cv2
from PIL import Image
from numpy import asarray

"""
# draw an image with detected objects
def draw_image_with_boxes(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
	# plot the image
	pyplot.imshow(data)
	# get the context for drawing boxes
	ax = pyplot.gca()
	# plot each box
	for result in result_list:
		# get coordinates
		x, y, width, height = result['box']
		# create the shape
		rect = Rectangle((x, y), width, height, fill=False, color='red')
		# draw the box
		ax.add_patch(rect)
		# draw the dots
		for key, value in result['keypoints'].items():
			# create and draw dot
			dot = Circle(value, radius=2, color='red')
			ax.add_patch(dot)
	# show the plot
	pyplot.show()
    """

folder = "F:\\suneel\\face count\\image_data\\"
#filenames = [item for sublist in [glob.glob(folder + ext) for ext in ["/*.png", "/*.jpg", "/*.jfif"]] for item in sublist]
data = pd.read_csv("F:\\suneel\\face count\\test_Rj9YEaI.csv")
#print(data.head())
#img = "F:\\suneel\\face count\\image_data\\10070.jpg"
images = []
    #print(filename)
    
#face_cascade = cv2.CascadeClassifier('F:\\Suneel\\face count\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')

for name in data["Name"]:
    filename = glob.glob(folder+name)
    for img in filename:
        image = Image.open(img)
        detector = MTCNN()
        image = image.convert('RGB')
        pixcel = asarray(image)
        faces = detector.detect_faces(pixcel)
        if len(faces) == 0:
            print("No Faces Found")
        else:
            #print(faces)
            #print(faces.shape)
            print("No of Faces: " + str(len(faces)))
            images.append(len(faces))
            
data1 = pd.DataFrame(images)
data1.columns = ["Count"]
data1["Name"] = data["Name"]
data2 = data1[["Name", "Count"]]
data2.to_csv("F:\\suneel\\face count\\final.csv")           

#draw_image_with_boxes(img, faces)