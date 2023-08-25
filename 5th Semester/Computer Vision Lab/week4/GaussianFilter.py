import cv2 as cv
img=cv.imread("C:/Users/OSLAB/Downloads/OIP.jpg")
cv.imshow('van gogh',img)
GaussBlurred=cv.GaussianBlur(img,(7,7),0)
cv.imshow('blurred gogh',GaussBlurred)
cv.waitKey(0)