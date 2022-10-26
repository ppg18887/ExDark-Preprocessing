#Moving Annotations to a single folder
import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
import shutil
import pandas as pd
os.chdir("/home/prathibha/object-detection-in-dark-images/")
ROOT_DIR = os.getcwd()

# create dict to map class names to numbers for yolo
classes = {}
with open("classes.txt", "r") as myFile:
    for num, line in enumerate(myFile, 0):
        line = line.rstrip("\n")
        classes[line] = num
    myFile.close()
    
# step into annotations directory
os.chdir('/home/prathibha/ExDark_Annno')
DIRS = os.listdir(os.getcwd())

print(classes)
print(DIRS)
print(os.getcwd())

for DIR in DIRS:

    if os.path.isdir(DIR):
        
        os.chdir(DIR)
        print("Currently in subdirectory:", DIR)


        for filename in tqdm(os.listdir(os.getcwd())):
            filename_str = str.split(filename, ".")[0]

            if filename.endswith(".txt"):
                annotations = []

                with open(filename) as f:
                    for l,line in enumerate(f):
                        if l==0:
                            continue
                        class_label = line.split()[0]
                        #excluded_classes =[]
                        if class_label.lower() not in list(classes.keys()):
                            #excluded_classes.append(class_label)
                            continue
                            
                        line = line.replace(class_label,class_label.lower())
                        
                        line = line.replace(class_label.lower(), str(classes[class_label.lower()]))

                        labels = line.split()
                        coords = np.asarray([float(labels[1]), float(labels[2]), float(labels[3]), float(labels[4])])
            
                        labels[1], labels[2], labels[3], labels[4] = coords[0], coords[1], coords[2], coords[3]
                        newline = str(labels[0]) + " " + str(labels[1]) + " " + str(labels[2]) + " " + str(labels[3]) + " " + str(labels[4])
                        line = line.replace(line, newline)
                        annotations.append(line)
                    f.close()
               
                with open(filename, "w") as outfile:
                    for line in annotations:
                        outfile.write(line)
                        outfile.write("\n")
                    outfile.close() 
    os.chdir("..")

