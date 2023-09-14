import cv2 as cv
import numpy as np
path="D:/labs/CV/images/skelly.png"
img=cv.imread(path)
laplace=cv.Laplacian(img,cv.CV_64F)
sharpened = cv.convertScaleAbs(laplace)
sharpening_factor = 0.5
laplSharp = cv.addWeighted(img, 1 + sharpening_factor, sharpened, -sharpening_factor, 0)

sobel_x=cv.Sobel(img,cv.CV_64F,1,0,0)
sobel_y=cv.Sobel(img,cv.CV_64F,0,1,0)
sqrt=np.sqrt(sobel_x**2+sobel_y**2)
sqrt=sqrt.astype(np.uint8)
sobelSharp=cv.addWeighted(img,1,sqrt,1,0)
sobelFinal=cv.GaussianBlur(sobelSharp,(5,5),1)

final=gamma_corrected=np.array(255*(sobelFinal/255)**1.5,dtype='uint8')
# final=gamma_corrected=np.array(255*(laplSharp/255)**1.5,dtype='uint8')

cv.imshow('original',img)
cv.imshow('laplaced',laplSharp)
cv.imshow('sobelled',sobelFinal)
cv.imshow('final',final)
cv.waitKey(0)