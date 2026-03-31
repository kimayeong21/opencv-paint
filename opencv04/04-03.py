import cv2
import numpy as np

img = cv2.imread('\python-opencv\lena.jpg', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 50, 100)

# Canny 에지 이미지에서 직선 검출
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100,
                        minLineLength=100, maxLineGap=10)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) # 컬러로 변환해 그리기

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()