import glob
import os
import shutil
src_folder = r"/content/video/MICC-F2000/"
dst_folder = r"/content/original/"
out_dir_path=r"/content/original/"
if not os.path.exists(out_dir_path):  #create folder if doesn't exist
    os.makedirs(out_dir_path)
for file in glob.glob('/content/video/MICC-F2000/*_scale.jpg'):
    shutil.move(file, dst_folder)