#Copying all annotation to pytorch folder
import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
import shutil
import pandas as pd
os.chdir("/home/prathibha/")
src_dir = "/home/prathibha/ExDark_ann_single"

os.chdir(src_dir)

des_dir = '/home/prathibha/PyTorch-YOLOv3/data/custom/labels/'

files = os.listdir(src_dir)


# chaging the file name to filename.txt format

for file in tqdm(files):
    
    lst = file.split('.')
    fname = lst[0]+'.'+lst[2]
    lines =[]
    with open(file) as f:
        for line in f:
            lines.append(line)
    os.chdir(des_dir)
    with open(fname, 'w') as fn:
        for line in lines:
            fn.write(line)
            #fn.write('\n')
        fn.close()
    os.chdir(src_dir)


