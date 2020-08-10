import cv2
import time


# Open Images
def open_images():
    img = cv2.imread("Resources/lena.jpg")

    cv2.imshow("lena", img)
    cv2.waitKey(0)


# Open Videos
def open_videos():
    cap = cv2.VideoCapture("Resources/Lava.mp4")
    # show cap
    show_img(cap)


# Open WebCam
def open_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)
    # show cap
    return show_img(cap)


def show_img(cap: cv2.VideoCapture):
    while cap.isOpened():
        success, img = cap.read()
        cv2.imshow("video", img)

        time.sleep(0.03)
        if cv2.waitKey(1) & 0xff == ord('q'):
            return True
    cap.release()
    return False


if __name__ == "__main__":
    print("this is main function")
    print("opening Image Lena...")
    open_images()
    print("opening Video Lava...")
    open_videos()
    print("opening WebCam...")
    if not open_webcam():
        print("WebCam not found")

    cv2.destroyAllWindows()
