import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lenna.png', 1)

M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 45, 0.7)
img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow('lenna', img_rotate)
key = cv2.waitKey(0)
cv2.destroyAllWindows()