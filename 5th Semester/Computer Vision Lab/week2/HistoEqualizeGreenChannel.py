import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path = "D:/labs/CV/images/rosie.jpg"
img = cv.imread(path)
b, g, r = cv.split(img)

g_equ = cv.equalizeHist(g)

# Merge the equalized green channel back into the original image
equalized_img = cv.merge((b, g_equ, r))

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.hist(g.ravel(), 256, [0, 256])
plt.title('Original Green Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equalized_img)
plt.title("Equalized Green Image")

plt.subplot(2, 2, 4)
plt.hist(g_equ.ravel(), 256, [0, 256])
plt.title('Equalized Green Histogram')

plt.tight_layout()
plt.show()
