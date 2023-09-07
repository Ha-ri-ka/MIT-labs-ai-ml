import cv2 as cv
import numpy as np
path="D:/labs/CV/images/brightspot.jpg"
img=cv.imread(path)
grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(grey)
cv.circle(img,max_loc,50 ,(0,0,0),2)        
cv.imshow('after',img)
cv.waitKey(0)
