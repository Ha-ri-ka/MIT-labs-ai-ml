import cv2 as cv
import numpy as np
path="D:/labs/CV/images/catto.png"
img=cv.imread(path)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lower_color=np.array([60,0,75])
upper_color=np.array([255,255,255])
color_mask=cv.inRange(hsv,lower_color,upper_color)
seg=cv.bitwise_and(img,img,mask=color_mask)
cv.imshow('',img)
cv.imshow('',seg)

cv.waitKey(0)