import cv2 as cv
import numpy as np
path='C:/Users/OSLAB/Desktop/images/smartie.jpg'
img=cv.imread(path)
cv.imshow('original',img)
c=255/(np.log(1+np.max(img)))
# print('max(img)=',np.max(img))
# print('c=',c)
log_trans=c*np.log(1+img) #formula for log transform
log_trans=np.array(log_trans,dtype=np.uint8)
cv.imshow('transformed',log_trans)
cv.waitKey(0)
