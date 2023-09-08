import cv2 as cv
import numpy as np
path="D:/labs/CV/images/hareKrishna.jpg"
img=cv.imread(path)
gauss=cv.GaussianBlur(img,(5,5),0)

def linearFilter(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width, _ = image.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width),(0,0)), mode='constant')
    filtered_image = np.zeros_like(image)
    for i in range(image_height):
        for j in range(image_width):
            patch = padded_image[i:i + kernel_height, j:j + kernel_width]
            filtered_image[i, j] = np.sum((patch * kernel)//9)
    return filtered_image


kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

filtered_image = linearFilter(img, kernel)
median_blur=cv.medianBlur(img,5)
cv.imshow('orig',img)
cv.imshow('gauss vlurred',gauss)
# cv.imshow('linear filter',filtered_image)
cv.imshow('median filter',median_blur)




cv.waitKey(0)