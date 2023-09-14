import cv2 as cv
import numpy as np
path="images/adaptive.png"
img=cv.imread(path,0)

def Threshold(img):
    hist,edges=np.histogram(img.ravel(),bins=256)
    tOld=edges.mean()
    deltaT=0.05
    while (True):
        firstHalf=img[img<tOld]
        secondHalf=img[img>=tOld]
        m1=np.mean(firstHalf)
        m2=np.mean(secondHalf)
        tNew=(m1+m2)/2
        diff=abs(tNew-tOld)
        if(diff<=deltaT): 
            break
        tOld=tNew
    _,Thresh=cv.threshold(img,tNew,255,cv.THRESH_BINARY)
    return Thresh

def adaptiveThreshold(img,n):
    '''divides the image into n*n equal parts'''
    part_width=img.shape[0]//n
    part_height=img.shape[1]//n
    parts=[]
    blank_image = np.zeros_like(img)
    for i in range(part_height):
        for j in range(part_width):
            y_start = i * part_height
            y_end = (i + 1) * part_height
            x_start = j * part_width
            x_end = (j + 1) * part_width
            part=img[y_start:y_end,x_start:x_end]
            if np.all(part == 0):
                continue
            partThresh=Threshold(part)
            blank_image[y_start:y_end,x_start:x_end]=partThresh
    return blank_image 

n=3
globalThresh=Threshold(img)
adaptiveThresh=adaptiveThreshold(img,n)
cv.imshow('original',img)
cv.imshow('simple global thresholding', globalThresh)
cv.imshow('adaptive thresholding', adaptiveThresh)
cv.waitKey(0)
