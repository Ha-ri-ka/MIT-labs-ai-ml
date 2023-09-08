import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path="D:/labs/CV/images/mid.jpg"
img=cv.imread(path)
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
    return tNew
thresh=Threshold(img)
truncThresh1 = np.where(img < thresh, img, 255).astype(np.uint8)
thresh2=Threshold(truncThresh1)
truncThresh2=np.where(truncThresh1 > thresh2, (truncThresh1), (0,0,255)).astype(np.uint8)
cv.imshow('thresh2',truncThresh2)
thresh2edges=cv.Canny(truncThresh2,thresh2,255)
mask=thresh2edges>0
# cv.imshow('',mask)
image_with_edges = np.copy(truncThresh2)
image_with_edges[mask]=[0,255,0]
cv.imshow('dges thresh',image_with_edges)
# thresh3=Threshold(truncThresh2)
# truncThresh3=np.where(truncThresh2 > thresh , (truncThresh2), (0,0,255)).astype(np.uint8)

plt.subplot(3,2,1)
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
plt.title('og image')
plt.subplot(3,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.title('og hist')
plt.subplot(3,2,3)
plt.imshow(cv.cvtColor(truncThresh1,cv.COLOR_BGR2RGB))
plt.title('thresh image')
plt.subplot(3,2,4)
plt.hist(truncThresh1.ravel(),256,[0,256])
plt.title('thresh hist')
plt.subplot(3,2,5)
plt.imshow(cv.cvtColor(truncThresh2,cv.COLOR_BGR2RGB))
plt.title('thresholding thresholded img')
plt.subplot(3,2,6)
plt.hist(truncThresh2.ravel(),256,[0,256])
plt.title('truncThresh2s hist')

# plt.subplot(3,2,7)
# plt.imshow(cv.cvtColor(truncThresh3,cv.COLOR_BGR2RGB))
# plt.title('truncthresh3')
# plt.subplot(3,2,8)
# plt.hist(truncThresh3.ravel(),256,[0,256])
# plt.title('thresh3 hist')
plt.show()
plt.tight_layout()
cv.waitKey(0)
