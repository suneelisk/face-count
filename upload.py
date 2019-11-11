from flask import *
import os
import sys
import xlwt
import xlrd
from xlrd import xldate_as_datetime
import pandas as pd
import openpyxl
from openpyxl import load_workbook
from datetime import datetime
import dateutil.parser as dparser
from matplotlib import pyplot
#from matplotlib.patches import Rectangle
#from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import pandas as pd
import glob
import numpy as np

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template("file_upload.html")

@app.route('/success', methods = ['GET', 'POST'])
def success():
    if request.method == 'POST':
        f = request.files['file1']
        if(f.filename!=''):
            f.save(os.path.join('F:\\Suneel\\face count project', f.filename))  #location where the uploaded file is stored

        filelocation='F:\\Suneel\\face count project\\' + f.filename

        book = pd.read_csv(filelocation)

        #To unmerge the merged cells
        folder = "F:\\Suneel\\face count project\\image_data\\"

        images = []
        for name in book["Name"]:
            filename = glob.glob(folder+name)
            for img in filename:
                image = pyplot.imread(img)
                detector = MTCNN()
                faces = detector.detect_faces(image)
                if len(faces) == 0:
                    print("No Faces Found")
                else:
                    print("No of Faces: " + str(len(faces)))
                images.append(len(faces))

        data1 = pd.DataFrame(images)
        """sum1 = np.sum(images)
        sum2 = book["HeadCount"].sum()
        print((sum1/sum2)*100)"""
        data1.columns = ["Pred"]
        data1["Name"] = book["Name"]
        #data1["HeadCount"] = book["HeadCount"]
        data2 = data1[["Name", "Pred"]]




        data2.to_csv("F:\\Suneel\\face count project\\media\\final1.csv")   #consolidated dataframe is written in this new file and in this location
        #Once the input file is selected and uploaded, processing is done and the consolidated file gets stored in the Downloads folder and the file is named Consolidated file.xlsx

        return render_template("success.html", tables=[data2.to_html(classes='data')], titles=data2.columns.values)#, tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug = True)
