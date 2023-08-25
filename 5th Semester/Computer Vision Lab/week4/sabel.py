import cv2 as cv
import numpy as np
path="C:/Users/OSLAB/Desktop/images/pattern.webp"
img=cv.imread(path)
sobel_x=cv.Sobel(img,cv.CV_64F,1,0,0)
sobel_y=cv.Sobel(img,cv.CV_64F,0,1,0)
sqrt=np.sqrt(sobel_x**2+sobel_y**2)
sqrt=sqrt.astype(np.uint8)
sqrrtt2=cv.addWeighted(img,1,sqrt,1,0)
cv.imshow('original',img)
cv.imshow('sharpened',sqrrtt2)
cv.waitKey(0)