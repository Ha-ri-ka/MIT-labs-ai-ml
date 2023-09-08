import cv2 as cv
import numpy as np
path="D:/labs/CV/images/mid.jpg"
img=cv.imread(path)

sobel_x=cv.Sobel(img,cv.CV_64F,1,0,0)
sobel_y=cv.Sobel(img,cv.CV_64F,0,1,0)
sqrt=np.sqrt(sobel_x**2+sobel_y**2)
sqrt=sqrt.astype(np.uint8)
sobelFinal=cv.addWeighted(img,1,sqrt,1,0)

laplacian = cv.Laplacian(img, cv.CV_64F)
sharpened = cv.convertScaleAbs(laplacian)
sharpening_factor = 0.5
laplaceFinal = cv.addWeighted(img, 1 + sharpening_factor, sharpened, -sharpening_factor, 0)
cv.imshow('og',img)
cv.imshow('sobel',sobelFinal)
cv.imshow('laplace',laplaceFinal)
cv.waitKey(0)