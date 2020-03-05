#!/usr/bin/env python
# coding: utf-8

# In[33]:


import tempfile
import os,shutil
import cv2


# In[34]:


from PIL import Image, ImageChops
ORIG = 'C:\\Users\\M1049186\\Desktop\\receipt.jpg'
SCALE = 10


# In[36]:


#create a  folder and save the copy of ORIG
directory = "Temp_Images" 
parent_dir = "C:\\Users\\M1049186\\Desktop\\copy_basics-master\\Project_name\\a_z project\\Fraudulent Detection"  
# Path 
path = os.path.join(parent_dir, directory) 
os.mkdir(path) 
print("Directory '% s' created" % directory)
#save image to path
copy_img = cv2.imread(ORIG)
status = cv2.imwrite('C:\\Users\\M1049186\\Desktop\\copy_basics-master\\Project_name\\a_z project\\Fraudulent Detection\\Temp_Images\\xyz.jpg',copy_img)
print("Temp Image created")
TEMP = 'C:\\Users\\M1049186\\Desktop\\copy_basics-master\\Project_name\\a_z project\\Fraudulent Detection\\Temp_Images\\xyz.jpg'


# In[37]:


def ELA():
    original = Image.open(ORIG)
    #original.save(TEMP, quality=90)
    temporary = Image.open(TEMP)

    diff = ImageChops.difference(original, temporary)
    d = diff.load()
    WIDTH, HEIGHT = diff.size
    for x in range(WIDTH):
        for y in range(HEIGHT):
            d[x, y] = tuple(k * SCALE for k in d[x, y])

    diff.save('C:\\Users\\M1049186\\Desktop\\fyu.jpg')
ELA()    
    
#classification model is done 


# In[5]:


#read the image in  folder and after that empty the  folder 
#import shutil

#dir_path = 'C:\\Users\\M1049186\\Desktop\\copy_basics-master\\Project_name\\a_z project\\Fraudulent Detection\\Temp_Images'

#try:
#    shutil.rmtree(dir_path)
#except OSError as e:
#    print("Error: %s : %s" % (dir_path, e.strerror))

