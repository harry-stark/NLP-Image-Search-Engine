import glob
import cv2
import os
import numpy as np

def pipeline(path:str):
     dir=glob.glob(os.path.join(path,"*.jpg"))+glob.glob(os.path.join(path,"*.png"))+glob.glob(os.path.join(path,"*.jpeg"))
     prep_img=[]
     for img in dir:
         z=cv2.imread(img)
         z=np.array(cv2.resize(z,(299,299)))
         prep_img.append(z)

     return dir,prep_img

