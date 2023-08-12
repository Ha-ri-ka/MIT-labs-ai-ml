import cv2  as cv
import numpy as np
path="D:/labs/CV/images/jennie.jpg"

def rescaleFrame(frame,scale=0.7):
    w=int(frame.shape[1]*scale)
    h=int(frame.shape[0] * scale)
    dim=(w,h)
    return cv.resize(frame,dim)

img=cv.imread(path)
negative=np.array(255-img,dtype=np.uint8)
pair=np.hstack((img,negative))
pair=rescaleFrame(pair)
cv.imshow('original vs negative',pair)
cv.waitKey(0)