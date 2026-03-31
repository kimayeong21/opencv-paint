# 허프 원 검출
import cv2
import numpy as np

# 🔥 경로 수정
src = cv2.imread('C:/python-opencv/shape.png')

if src is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 🔥 노이즈 제거 추가 (중요)
gray = cv2.GaussianBlur(gray, (9, 9), 2)

# 🔥 HoughCircles 수정
circles1 = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,   # 필수🔥
    dp=1,
    minDist=50,
    param1=120,
    param2=15,
    minRadius=10,
    maxRadius=100
)

# 🔥 None 체크 (필수)
if circles1 is not None:
    circles1 = np.int32(circles1)
    print('circles1.shape=', circles1.shape)

    for circle in circles1[0, :]:
        cx, cy, r = circle
        cv2.circle(src, (cx, cy), r, (0, 0, 255), 2)
else:
    print("원을 찾지 못했습니다.")

cv2.imshow('src', src)

cv2.waitKey(0)
cv2.destroyAllWindows()