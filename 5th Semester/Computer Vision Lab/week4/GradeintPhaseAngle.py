import cv2 as cv
import numpy as np
path="C:/Users/OSLAB/Desktop/images/blank.webp"
img=cv.imread(path)
gradient_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
gradient_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_phase = np.arctan2(gradient_y, gradient_x)
gradient_phase_degrees = np.degrees(gradient_phase)
cv.imshow('Gradient Magnitude', gradient_magnitude.astype(np.uint8))
cv.imshow('Gradient Phase Angle', gradient_phase_degrees.astype(np.uint8))
cv.imshow('original',img)
cv.waitKey(0)
cv.destroyAllWindows()