import cv2
import numpy as np

src = cv2.imread('\python-opencv\lena.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 빨간색 추출 예시 (H: 0~10 or 170~180)
# 빨간색은 Hue 값이 0 근처와 180 근처 양쪽에 걸쳐 있습니다.
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
