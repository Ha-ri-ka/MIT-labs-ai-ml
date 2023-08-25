import cv2
import numpy as np
path="C:/Users/OSLAB/Desktop/images/pattern.webp"
image = cv2.imread(path)
laplacian = cv2.Laplacian(image, cv2.CV_64F)
sharpened = cv2.convertScaleAbs(laplacian)
sharpening_factor = 0.5
sharpened_image = cv2.addWeighted(image, 1 + sharpening_factor, sharpened, -sharpening_factor, 0)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()