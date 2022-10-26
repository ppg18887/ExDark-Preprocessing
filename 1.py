#Moving all files to Pytorch Yolo folder
import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
import shutil
import pandas as pd
os.chdir('/home/prathibha/Downloads/ExDark/ExDark/ExDark')
dest_dir = "/home/prathibha/PyTorch-YOLOv3/data/custom/images"
DIRS=os.listdir('/home/prathibha/Downloads/ExDark/ExDark/ExDark/')
print(DIRS)
for DIR in DIRS:
    if os.path.isdir(DIR):
        
        print("Currently in subdirectory:", DIR)

        # path to source directory
        src_dir = DIR

        # getting all the files in the source directory
        files = os.listdir(src_dir)
        
        for fname in tqdm(files):
     
            # copying the files to the
            # destination directory
            shutil.copy2(os.path.join(src_dir,fname), dest_dir)

