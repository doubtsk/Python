import numpy as np
import cv2
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 10))
img = cv2.imread("C:\\Python\\image\\0.png")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height = grayImage.shape[0]
width = grayImage.shape[1]
result = np.zeros((height, width), np.uint8)

for i in range(width):
    for j in range(width):
        cvt = int(grayImage[i, j]*1.3-30)
        if (cvt > 255):
            gray = 255
        elif (cvt < 0):
            gray = 0
        else:
            gray = cvt
        result[i, j] = np.uint8(gray)
plt.subplot(121)
plt.imshow(grayImage, cmap='gray')
plt.title("Gray Image")

plt.subplot(122)
plt.imshow(grayImage, cmap='gray')
plt.title("Result")
