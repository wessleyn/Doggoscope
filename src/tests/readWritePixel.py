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


def readAndWritePixelRegion():
    imgPath = os.path.join(ROOT, "demoImages", "cutePic1.jpeg")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    x_1 = 304  
    y_1 = 237 

    x_2 = 330
    y_2 = 259

    eyeRegion = imgRGB[y_1:y_2, x_1:x_2]
    regionColor = (0, 255, 0)  
    regionOutlineThickness = 2

    cv.rectangle(imgRGB, (x_1, y_1), (x_2, y_2), regionColor, regionOutlineThickness)

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(imgRGB)
    plt.title("Eye Region Highlighted")

    plt.subplot(1, 2, 2)
    plt.imshow(eyeRegion)
    plt.title("Extracted Eye Region")
    plt.show()

if __name__ == "__main__":
    # readAndWriteSinglePixel()
    readAndWritePixelRegion()
