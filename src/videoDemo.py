import os

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

CAMERA_INDEX = 0


def videoFromCam():
    cap = cv.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        else:
            cv.imshow("frame", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    videoFromCam()
