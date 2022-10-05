import os
import numpy as np
import shutil
import random
#Creating directories
original_folder="/home/prathibha/Downloads/Data_Main"
train_folder="/home/prathibha/Downloads/Data/train"
validation_folder="/home/prathibha/Downloads/Data/validation"
test_folder="/home/prathibha/Downloads/Data/test"
os.mkdir(train_folder)
os.mkdir(validation_folder)
os.mkdir(test_folder)
allFileNames = os.listdir(original_folder)
np.random.shuffle(allFileNames)
## here 0.75 = training ratio , (0.95-0.75) = validation ratio , (1-0.95) =  
##training ratio  
train_FileNames,val_FileNames,test_FileNames = np.split(np.array(allFileNames),[int(len(allFileNames)*0.75),int(len(allFileNames)*0.95)])
# #Converting file names from array to list
train_FileNames = [original_folder+'/'+name for name in train_FileNames]
val_FileNames = [original_folder+'/'+name for name in val_FileNames]
test_FileNames = [original_folder+'/'+name for name in test_FileNames]
print('Total images  : ' + ' ' +str(len(allFileNames)))
print('Training : ' + ' '+str(len(train_FileNames)))
print('Validation : '+ ' ' +str(len(val_FileNames)))
print('Testing : '+ ' '+str(len(test_FileNames)))
for name in train_FileNames:
	shutil.copy(name, train_folder)
for name in val_FileNames:
	shutil.copy(name, validation_folder)
for name in test_FileNames:
	shutil.copy(name, test_folder)
