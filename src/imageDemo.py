import os

import cv2 as cv
import matplotlib.pyplot as plt  # type: ignore
import numpy as np

ROOT = os.path.abspath("../assets/")

def readImage():
    imgPath = os.path.join(ROOT, "demoImages", "cutePic1.jpeg")
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow("img", img)
    cv.waitKey(0)

def writeImage():
    imgPath = os.path.join(ROOT, "demoImages", "cutePic1.jpeg")
    img = cv.imread(imgPath)
    os.makedirs(os.path.join(ROOT, "output"), exist_ok=True)
    writePath = os.path.join(ROOT, "output", "output.png")
    cv.imwrite(writePath, img)

if __name__ == "__main__":
    print(cv.__version__)
    # readImage()
    writeImage()