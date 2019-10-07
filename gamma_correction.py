import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lenna.png', 1)


def gamma_adjust(img, gamma=1.0):
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** gamma) * 255)
    table = np.array(table).astype('uint8')
    img_gamma = cv2.LUT(img, table)  # 旧图片映射到table
    return img_gamma


# change color
img_gamma = gamma_adjust(img, gamma=2.5)
cv2.imshow('lenna', img_gamma)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
