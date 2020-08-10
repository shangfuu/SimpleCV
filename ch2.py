# Chapter2: Basic Functions
import cv2
import numpy as np
import time

img = cv2.imread("Resources/lena.jpg")

# Convert to Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur
imgBlur = cv2.GaussianBlur(img, (5, 5), 3)
# Canny
imgCanny = cv2.Canny(img, 150, 200)
# Dilate
# imgDilate = cv2.dilate(imgCanny, kernel=(5, 5), iterations=1)
kernel = np.ones((5, 5), np.uint8)
imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)
# Erode
imgErode = cv2.erode(imgDilate, kernel, iterations=1)

images = [("origin", img), ("Gray", imgGray), ("Blur", imgBlur), ("Canny", imgCanny), ("Dilate", imgDilate), ("Erode", imgErode)]

# Show images
for name, i in images:
    cv2.imshow(name, i)
    cv2.waitKey(2000)
    cv2.destroyWindow(name)

cv2.waitKey(0)
