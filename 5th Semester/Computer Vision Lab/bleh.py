import cv2 as cv
import numpy as np
path="C:/Users/OSLAB/Desktop/2030B/midtermexam/image (87).jpg"
img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
# def Threshold(img):
#     hist,edges=np.histogram(img.ravel(),bins=256)
#     tOld=edges.mean()
#     deltaT=0.05
#     while (True):
#         firstHalf=img[img<tOld]
#         secondHalf=img[img>=tOld]
#         m1=np.mean(firstHalf)
#         m2=np.mean(secondHalf)
#         tNew=(m1+m2)/2
#         diff=abs(tNew-tOld)
#         if(diff<=deltaT): 
#             break
#         tOld=tNew
#     return tNew

# equ=cv.equalizeHist(gray)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray)
final = np.where(img >= (max_val), (0,255,0), img).astype(np.uint8)
# thresh=Threshold(img)
# binaryThresh = np.where(img < thresh, 0, 255).astype(np.uint8)
# truncateThresh = np.where(img < thresh, img, (0,255,0)).astype(np.uint8)
# toZeroThresh = np.where(img < thresh, 0, img).astype(np.uint8)
# cv.imshow('bin',binaryThresh)
# cv.imshow('trunc',truncateThresh)
# cv.imshow('tozero',toZeroThresh)
# image=img.copy()
# cv.circle(image,max_loc,50 ,(0,0,0),2)
cv.imshow('original',img)
cv.imshow('final',final)
# cv.imshow('bright',image)
# cv.imshow('equ',equ)
cv.waitKey(0)
cv.destroyAllWindows()
