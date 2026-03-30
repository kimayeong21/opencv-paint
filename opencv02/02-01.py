import cv2
import numpy as np

src = cv2.imread('\python-opencv\lena.jpg')
val = 100 # 더할 밝기 값

# OpenCV 함수 이용 (추천) -> 밝아짐
dst1 = cv2.add(src, (val, val, val, 0))

# numpy 연산 이용 -> 255 넘으면 깨짐
dst2 = src + val

cv2.imshow('OpenCV Add', dst1)
cv2.imshow('Numpy Add', dst2)
cv2.waitKey()
cv2.destroyAllWindows()