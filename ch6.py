# Chapter6: Joining Images

import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
card = cv2.imread("Resources/cards.jpg")


# Must be the same size, even channel
def simple_join():
    """
    # this will lead to crash
    imgHor = np.hstack((img, card))
    """

    # Image horizontal join
    imgHor = np.hstack((img, img))
    cv2.imshow("hor", imgHor)

    # Image Vertical join
    imgVer = np.vstack((img, img))
    cv2.imshow("ver", imgVer)


# Can be join even if the channel wasn't the same
def stackImages(scale, imgArray):
    # rows and cols of imgArray
    rows = len(imgArray)
    cols = len(imgArray[0])
    # check if imgArray is a list
    rowsAvailable = isinstance(imgArray[0], list)
    # take the first image as the criteria
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        # Loop for each pic in imgArray and do reshape or check if grayscale then convert to BGR
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], None, None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imgBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imgBlank] * rows
        print(np.shape(hor))
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


if __name__ == "__main__":
    simple_join()
    # Make a grayscale lena
    grayLena = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgStack = stackImages(0.5, ([img, grayLena, img], [img, card, img]))
    cv2.imshow("stackImages", imgStack)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
