import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.rectangle(blank,(0,0),(250,500),(255,255,255),5)
cv.imshow('blank',blank)
cv.waitKey(0)