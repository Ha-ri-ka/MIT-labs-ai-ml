import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path='C:/Users/OSLAB/Desktop/images/histo.jpg'

img=cv.imread(path,0)
equ=cv.equalizeHist(img)
pair=np.hstack((img,equ))
cv.imwrite('original vs equalized.jpg',pair)
#ravel-->used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array.
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.hist(img.ravel(),256,[0,256],color='pink')
plt.title('Original Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')

plt.subplot(2, 2, 4)
plt.hist(equ.ravel(),256,[0,256],color='pink')
plt.title('Equalized Histogram')

plt.tight_layout()
plt.show()

