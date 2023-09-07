import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path="D:/labs/CV/images/threshold.jpg"
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
binaryThresh = np.where(img < thresh, 0, 255).astype(np.uint8)
truncateThresh = np.where(img < thresh, img, thresh).astype(np.uint8)
toZeroThresh = np.where(img < thresh, 0, img).astype(np.uint8)

plt.figure(figsize=(10,8))

plt.subplot(4,2,1)
plt.imshow(img)
plt.title('Original image')

plt.subplot(4,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.title('Original image histogram')

plt.subplot(4,2,3)
plt.imshow(binaryThresh)
plt.title('Binary Thresholded image')

plt.subplot(4,2,4)
plt.hist(binaryThresh.ravel(),256,[0,256])
plt.title('Thresholded image histogram')

plt.subplot(4,2,5)
plt.imshow(truncateThresh)
plt.title('Truncate Thresholded image')

plt.subplot(4,2,6)
plt.hist(truncateThresh.ravel(),256,[0,256])
plt.title('Truncate thresholded image histogram')

plt.subplot(4,2,7)
plt.imshow(toZeroThresh)
plt.title('To zero Thresholded image')

plt.subplot(4,2,8)
plt.hist(toZeroThresh.ravel(),256,[0,256])
plt.title('To zero thresholded image histogram')

plt.tight_layout()
plt.show()
