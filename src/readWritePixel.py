import os

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.abspath("./assets/")


def readAndWriteSinglePixel():
    imgPath = os.path.join(ROOT, "demoImages", "cutePic1.jpeg")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.title("Original Image")
    plt.show()

    [x, y] = 316, 247
    redColor = [255, 0, 0]  
    circleRadius = 5
    
    cv.circle(imgRGB, (x, y), circleRadius, redColor, -1)

    plt.figure(figsize=(10, 8))
    plt.imshow(imgRGB)
    plt.title(f"Red dot at position ({x}, {y})")
    plt.show()


if __name__ == "__main__":
    readAndWriteSinglePixel()
