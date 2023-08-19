import cv2 as cv
img=cv.imread("resources/vangogh.webp")
cv.imshow('original',img)
rotated=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
cv.imshow('rotated',rotated)
cv.waitKey(0)
