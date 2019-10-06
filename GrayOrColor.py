import cv2
import matplotlib.pyplot as plt

#color image
img = cv2.imread('lenna.png', 1)
cv2.imshow('lenna', img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()

#gray image
img_gray = cv2.imread('lenna.png', 0)
cv2.imshow('lenna', img_gray)
key = cv2.waitKey(0)
cv2.destroyAllWindows()

#opencv顺序BGR，matplotlib顺序RGB
B, G, R = cv2.split(img)
img_new = cv2.merge((R, G, B))
plt.imshow(img_new)
plt.show()