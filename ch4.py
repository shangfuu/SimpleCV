# Chapter4: Shapes and Texts

import cv2
import numpy as np


def show_block():
    img = np.zeros((512, 512, 3), np.uint8)
    img[0:87, 0:187, 0] = 255
    img[0:87, 0:87, 2] = 87
    print(img[0:87, 0:87])
    cv2.imshow("block", img)


def show_line():
    img = np.zeros((512, 256, 3), np.uint8)
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
    cv2.imshow("line", img)


def show_rect():
    img = np.zeros((512, 256, 3), np.uint8)
    cv2.rectangle(img, (89, 87), (250, 187), (87, 87, 87), 3)
    cv2.imshow("rect", img)


def show_circle():
    img = np.zeros((512, 256, 3), np.uint8)
    cv2.circle(img, (89, 117), 10, (87, 87, 87), 3)
    cv2.imshow("circle", img)


def show_text():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.putText(img, "OPENCV", (287, 287), cv2.FONT_ITALIC, 2, (187, 87, 177), 2)
    cv2.imshow("Text", img)


if __name__ == "__main__":
    show_block()
    show_line()
    show_rect()
    show_circle()
    show_text()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
