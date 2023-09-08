import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path="D:/labs/CV/images/vangogh.webp"
img=cv.imread(path)
gamma=np.array(255*(img/255)**0.5,dtype='uint8')
c=255/(np.log(1+np.max(img)))
log_trans=c*np.log(1+img) #formula for log transform
log_trans=np.array(log_trans,dtype=np.uint8)
negative=np.array(255-img,dtype=np.uint8)

cv.imshow('original',img)
# cv.imshow('gamma',gamma)
# cv.imshow('log',log_trans)
cv.imshow('negative',negative)
cv.waitKey(0)