# normalizing the bounding box values to [0,1]
import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
import shutil
import pandas as pd
def convert(img_w,img_h, box):

    x = box[0] + (box[2]/2.0)
    y = box[1] + (box[3]/2.0)

    x = x/img_w
    y = y/img_h
    
    w = box[2]/img_w
    h = box[3]/img_h

    return x,y,w,h

img_dir = '/home/prathibha/PyTorch-YOLOv3/data/custom/images/'

txt_dir = '/home/prathibha/PyTorch-YOLOv3/data/custom/labels/'

images_files = os.listdir(img_dir)

txt_files = os.listdir(txt_dir)

for image in tqdm(images_files):
    if os.path.isfile(img_dir+image):
        img = cv2.imread(os.path.join(img_dir,image))
        img_h , img_w, _ = img.shape

        fname = image.split('.')[0]
        fname = fname+'.txt'
        txt_file = os.path.join(txt_dir,fname)
        lines =[]
        with open(txt_file) as f:
            for line in f:
                labels = line.split()
                labels[0]= int(labels[0])
                labels[1],labels[2],labels[3],labels[4] = float(labels[1]),float(labels[2]),float(labels[3]),float(labels[4])
                box = [labels[1],labels[2],labels[3],labels[4]]
                labels[1],labels[2],labels[3],labels[4] = convert(img_w,img_h,box)
                new_line = ' '.join(str(i) for i in labels)
                line = line.replace(line,new_line)
                lines.append(line)
            f.close()
        with open(txt_file,'w') as fw:
            for line in lines:
                fw.write(line)
                fw.write("\n")
            fw.close()
