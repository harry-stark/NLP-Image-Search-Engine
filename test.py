import os
import time
st=time.time()
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from engine import models
from engine import pipeline
from engine.genrator import generator,querygen,find_match
#way = input("Image Directory")
imgem=None
filelist=None
imgem,filelist=generator("/home/harry/Documents/Engine2/images")
print(len(imgem))
query=['desert']
quem=querygen(query)
rs=find_match(imgem,quem,2)
print(rs)
print(filelist)
print(type(imgem))
print("                                           profileing             ")


end=time.time()

print(end-st,"time taken ")