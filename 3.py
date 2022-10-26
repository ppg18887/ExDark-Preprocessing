#copying all annotations to one folder
import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
import shutil
import pandas as pd
os.chdir("/home/prathibha/ExDark_Annno/")
ROOT_DIR = os.getcwd()


DIRS = os.listdir(os.getcwd())

print(DIRS)
print(os.getcwd())

dest_dir = "/home/prathibha/ExDark_ann_single"


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
