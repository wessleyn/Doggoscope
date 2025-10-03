import os

import cv2 as cv
import matplotlib.pyplot as plt  # type: ignore
import numpy as np


def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root, "../assets/demoImages", "cutePic1.jpeg")
    img = cv.imread(imgPath)
    cv.imshow("Cute Pic", img)
    cv.waitKey(0)

if __name__ == "__main__":
    print(cv.__version__)
    readImage()