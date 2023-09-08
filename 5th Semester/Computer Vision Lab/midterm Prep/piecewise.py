import cv2 as cv
import numpy as np
path="C:/Users/OSLAB/Desktop/images/histo.jpg"
img=cv.imread(path)
def pixelVal(pix,r1,s1,r2,s2):
    if(0<=pix and pix<=r1):
        return (s1/r1)*pix
    elif(r1<pix and pix<=r2):
        return((s2-s1)/(r2-r1))*(pix-r1)+s1
    else:
        return((255-s2)/(255-r2))*(pix-r2)+s2
r1,s1,r2,s2=70,0,140,255
pixelVal_vec=np.vectorize(pixelVal)
contrast_stretched=pixelVal_vec(img,r1,s1,r2,s2)
cv.imshow('transformed',contrast_stretched)
cv.imshow('original',img)
cv.waitKey(0)
cv.destroyAllWindows()