# Chapter8: Contours / Shape Detection
import cv2
import numpy as np
from ch6 import stackImages

def getContours(imgCanny, imgContour):
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 30:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)

            # Get the point of corner
            peri = cv2.arcLength(cnt, True)
            poly = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            # Showing the number of corner
            cornerNum = len(poly)
            print(cornerNum)

            # Get the bounding box
            x, y, w, h = cv2.boundingRect(poly)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Name the shape
            if cornerNum == 3:
                objType = "Tri"
            elif cornerNum == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.9 and aspRatio < 1.1:
                    objType = "Spuare"
                else:
                    objType = "Rectangle"
            elif cornerNum == 6:
                objType = "6corner"
            else: objType = "Circle?"

            cv2.putText(imgContour, objType, (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 2)


img = cv2.imread("Resources/shape.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 2)

imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

imgContour = img.copy()
getContours(imgCanny, imgContour)

imgStack = stackImages(0.7, [[img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]])
cv2.imshow("stack", imgStack)

cv2.waitKey(0)