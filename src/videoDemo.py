import os

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

CAMERA_INDEX = 0
ROOT = os.path.abspath("../assets/")


def videoFromCam():
    cap = cv.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        else:
            cv.imshow("frame", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


def videoFromFile():
    root = os.getcwd()
    videoPath = os.path.join(root, "assets", "demoVideos", "mirrorChasing.mp4")
    cap = cv.VideoCapture(videoPath)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        else:
            cv.imshow("frame", frame)

        if cv.waitKey(16) == ord("q"):
            break


if __name__ == "__main__":
    # videoFromCam()
    videoFromFile()
