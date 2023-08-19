import cv2 as cv
img=cv.imread("D:/labs/CV/images/vangogh.webp")
cv.imshow('original',img)
resized=cv.resize(img,(200,200))
cropped=img[50:200,200:400]
cv.imshow('resized',resized)
cv.imshow('cropped',cropped)
cv.waitKey(0)
