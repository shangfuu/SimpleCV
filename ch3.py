# Chapter3: Resizing and Cropping

import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
print(img.shape)
cv2.imshow("org", img)

imgResize = cv2.resize(img, (256, 256))
print(imgResize.shape)
cv2.imshow("resize", imgResize)

imgCropped = img[40:200, 30:300]
print(imgCropped)
cv2.imshow("crop", imgCropped)

cv2.waitKey(0)
