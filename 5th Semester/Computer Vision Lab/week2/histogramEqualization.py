import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path='C:/Users/OSLAB/Desktop/images/histo.jpg'

img=cv.imread(path,0)
equ=cv.equalizeHist(img)
pair=np.hstack((img,equ))
cv.imwrite('original vs equalized.jpg',pair)
cv.waitKey(0)
#ravel-->used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array.
plt.hist(img.ravel(),256,[0,256])
plt.hist(equ.ravel(),256,[0,256])
plt.title('histogram')
plt.legend(['original','equalized'])
plt.show()

