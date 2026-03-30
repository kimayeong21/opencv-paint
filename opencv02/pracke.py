import cv2
import numpy as np

# 이미지 불러오기
src = cv2.imread('\python-opencv\lena.jpg')   # 녹색 배경 이미지
bg = cv2.imread('\python-opencv\lena.jpg')     # 배경 이미지

if src is None or bg is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

# 크기 맞추기
src = cv2.resize(src, (400, 400))
bg = cv2.resize(bg, (400, 400))

# HSV 변환
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
mask_inv = cv2.bitwise_not(mask)

# -------------------------------
# 1️⃣ 녹색 제거된 이미지
# -------------------------------
foreground = cv2.bitwise_and(src, src, mask=mask_inv)

# -------------------------------
# 2️⃣ lena 위에 검은 피사체
# -------------------------------
# 검은 이미지 생성
black = np.zeros_like(src)

# 피사체만 검게 추출
black_subject = cv2.bitwise_and(black, black, mask=mask_inv)

# lena에서 해당 위치만 남기기
bg_part = cv2.bitwise_and(bg, bg, mask=mask)

# 합치기
black_result = cv2.add(bg_part, black_subject)

# -------------------------------
# 3️⃣ 정상 합성
# -------------------------------
background = cv2.bitwise_and(bg, bg, mask=mask)
result = cv2.add(foreground, background)

# 출력
cv2.imshow('foreground', foreground)
cv2.imshow('black on lena', black_result)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()