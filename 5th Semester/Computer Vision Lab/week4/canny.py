import cv2 as cv
import numpy as np
path="C:/Users/OSLAB/Desktop/images/pattern.webp"
img=cv.imread(path)
cv.imshow("ori",img)
canny=cv.Canny(img,180,190)
cv.imshow('Canny',canny)
cv.waitKey(0)
cv.destroyAllWindows()