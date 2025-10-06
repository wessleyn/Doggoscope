import os

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

CAMERA_INDEX = 0
ROOT = os.path.abspath("../assets/")
FRPS = 20
HEIGHT = 480
WIDTH = 640

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
    videoPath = os.path.join(ROOT, "demoVideos", "mirrorChasing.mp4")
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

def writeVideoToFile():
    cap = cv.VideoCapture(CAMERA_INDEX)

    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    outPath = os.path.join(ROOT, "output", "webcam.mp4")
    out = cv.VideoWriter(outPath, fourcc, FRPS, (WIDTH, HEIGHT))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        else:
            out.write(frame)
            cv.imshow("frame", frame)

        if cv.waitKey(16) == ord("q"):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()
if __name__ == "__main__":
    # videoFromCam()
    # videoFromFile()
    writeVideoToFile()
