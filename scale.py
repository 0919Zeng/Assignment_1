import cv2

img = cv2.imread('lenna.png', 0)

height, width = img.shape[:2]
res = cv2.resize(img, (3*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('lenna', res)
key = cv2.waitKey(0)
cv2.destroyAllWindows()