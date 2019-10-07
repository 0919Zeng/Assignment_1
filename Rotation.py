import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lenna.png', 1)

M = cv2.getRotationMatrix2D((0, 0), 15, 0.9) #以（0，0）为中心旋转15度，放大0.9倍
img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow('lenna', img_rotate)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
