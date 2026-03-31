# practice-easy.py
# 정해진 이미지의 정해진 좌표값을 하드코딩하는 방식
import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread("\python-opencv\djkflsa.jpg")
rows, cols, ch = src.shape

# 이동하기 전 원래 위치
pts1 = np.float32([
    [57, 24],
    [416, 14],
    [16, 528],
    [467, 522]])

# 이동하고 나서의 위치
pts2 = np.float32([
    [0,0],
    [cols,0],
    [0,rows],
    [cols, rows]])

cv2.circle(src, (57, 24), 10, (255,0,0),-1)
cv2.circle(src, (416, 14), 10, (0,255,0),-1)
cv2.circle(src, (16, 528), 10, (0,0,255),-1)
cv2.circle(src, (467, 522), 10, (255,0,255),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(src, M, (cols,rows))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()