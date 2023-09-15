import cv2 as cv
import numpy as np
path="C:/Users/OSLAB/Desktop/images/cube.jpg"
img=cv.imread(path)
final=img.copy()
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
corner=cv.cornerHarris(gray,5,5,0.04)
final[corner>0.01*corner.max()]=[0,0,255]
cv.imshow('original',img)
cv.imshow('corners',final)
cv.waitKey(0)
