import cv2 as cv
path="C:/Users/OSLAB/Desktop/images/leaf.webp"
img=cv.imread(path)
cv.imshow('van gogh',img)
GaussBlurred=cv.GaussianBlur(img,(3,3),0)
temp=cv.subtract(img,GaussBlurred)
sharp=cv.add(img,temp)
# sharp=img+(img-GaussBlurred)
cv.imshow('sharpened',sharp)
cv.waitKey(0)