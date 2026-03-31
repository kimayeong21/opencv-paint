import cv2
import numpy as np

img = cv2.imread('\python-opencv\lena.jpg', cv2.IMREAD_GRAYSCALE)

# dx=1, dy=0: 수직 에지 검출
sobel_x = cv2.Sobel(img, -1, 1, 0, ksize=3)

# dx=0, dy=1: 수평 에지 검출
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize=3)

cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()