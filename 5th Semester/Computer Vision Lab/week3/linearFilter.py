import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_linear_filter(image, kernel):
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

path = "D:/labs/CV/images/vangogh.webp"
image = cv2.imread(path)

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

filtered_image = apply_linear_filter(image, kernel)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title('Filtered Image')

plt.tight_layout()
plt.show()