import cv2 as cv
import numpy as np
path='C:/Users/OSLAB/Desktop/images/smartie.jpg'
# gamma=0.5
img=cv.imread(path)
cv.imshow('original',img)
for gamma in [0.1,0.5,1.2,2.2]:
    gamma_corrected=np.array(255*(img/255)**gamma,dtype='uint8')
    cv.imwrite('trans'+str(gamma)+'.jpg',gamma_corrected)
cv.imshow(str(gamma)+' transformed',gamma_corrected)
cv.waitKey(0)