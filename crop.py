import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lenna.png', 1)
#打印尺寸 (512,512,3)
print(img.shape)

img_crop = img[100:300, 200:400]
cv2.imshow('lenna', img_crop)
key = cv2.waitKey(0)
cv2.destroyAllWindows()