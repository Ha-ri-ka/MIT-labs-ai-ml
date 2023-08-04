import cv2 as cv
import numpy as np

img=cv.imread('C:/Users/OSLAB/Downloads/OIP.jpg')
b,g,r=cv.split(img)
#print(b)
#cv.imshow('b vg',b)
blank=np.zeros(b.shape,dtype='uint8')

red_img=cv.merge((blank,blank,r))
blue_img=cv.merge((b,blank,blank))
green_img=cv.merge((blank,g,r))

cv.imshow('red vg',red_img)
cv.imshow('blue vg',blue_img)
cv.imshow('green vg',green_img)
cv.waitKey(0)
