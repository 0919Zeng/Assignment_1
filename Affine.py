import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lenna.png', 0)

rows, cols = img.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.3, rows * 0.4], [cols * 0.6, rows * 0.2], [cols*0.1, rows * 0.9]])

M = cv2. getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('lenna', dst)
key = cv2.waitKey(0)
cv2.destroyAllWindows()