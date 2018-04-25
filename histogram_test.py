import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/minch/OneDrive/Documents/BME370-DESKTOP-QM1PTM9/Code/test_strip.jpg')

#hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([img], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist,interpolation = 'nearest')
plt.show()	