# Chapter7: Color Detection
import cv2
import numpy as np


def trackFunction(e):
    pass


def createTrackWindow():
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    # Set initial value as what you modified
    cv2.createTrackbar("Hue Min", "TrackBars", 24, 179, trackFunction)
    cv2.createTrackbar("Hue Max", "TrackBars", 64, 179, trackFunction)
    cv2.createTrackbar("Sat Min", "TrackBars", 43, 255, trackFunction)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, trackFunction)
    cv2.createTrackbar("Val Min", "TrackBars", 53, 255, trackFunction)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, trackFunction)


def getTrackbarPos():
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    return hue_min, hue_max, sat_min, sat_max, val_min, val_max


if __name__ == "__main__":
    img = cv2.imread("Resources/lambo.jpg")
    # HSV: Hue, Saturation, Value
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("Origin", img)
    cv2.imshow("HSV", imgHSV)

    createTrackWindow()

    while True:
        h_min, h_max, s_min, s_max, v_min, v_max = getTrackbarPos()
        print(h_min, h_max, s_min, s_max, v_min, v_max)

        # Getting the mask
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        # Mask the origin image
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        cv2.imshow("Mask", mask)
        cv2.imshow("Result", imgResult)
        cv2.waitKey(1)
