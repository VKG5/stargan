#!/usr/bin/env python
# coding: utf-8

# ## To segregate the files into test and train folder

# In[2]:


# Importing the libraries
import os
import glob
import shutil
import cv2


# In[3]:


# Setting the directories
# Directory of the .ipynb file
base = os.getcwd()

# Folder/Directory of the images folder
rafd = "\RaFD"

# Base directory of images
base = base+rafd

test_dir = base+"\\test\\"
train_dir = base+"\\train\\"

print(base)
print(test_dir)
print(train_dir)


# In[37]:


# Making the required lists
# Available emotions
""" happy
angry
sad
contemptuous
disgusted
neutral
fearful
surprised """

data_path = os.path.join(base,'*g')
print(data_path)
files = glob.glob(data_path)
images_list = []
count=0

# For loafing the names of all the images
for f1 in files:
    # f1 = f1.replace((base+"\\"),"")
    images_list.append(f1)
    # print(count)
    count+=1

tot_num = len(images_list)
print(tot_num)


# ## Shifting the pics code

# In[38]:


# Printing the name for different images
for img in images_list:
    print(img)


# In[39]:


emotions = {"happy","angry","sad","contemptuous","disgusted","neutral","fearful","surprised"}

print(train_dir)
for emo in emotions:
    dir = train_dir+emo+"\\"
    # print(dir)
    for img in images_list:
        if(img.find(emo)!=-1):
            # print(img)
            shutil.copy(img, dir)
    ## print("\n\n")

print("Done :D")


# In[ ]:




