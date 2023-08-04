import cv2 as cv
def rescaleFrame(frame,scale=2):
    w=(frame.shape[1]*scale)
    h= (frame.shape[0] * scale)
    dim=(w,h)
    return cv.resize(frame,dim)

img=cv.imread('C:/Users/OSLAB/Downloads/OIP.jpg')
cv.imshow('before resize',img)
cv.imshow('after resize',rescaleFrame(img))

cv.waitKey(0)