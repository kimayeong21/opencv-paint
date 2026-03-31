import cv2
import numpy as np

# 1. 이미지 불러오기
src = cv2.imread('C:/python-opencv/coins.jpg')
if src is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

result = src.copy()

# 2. 전처리: 색상 변환 및 노이즈 제거
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. 이진화 (배경과 동전 분리)
thresh = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    51,
    7
)

# 4. 노이즈 제거: 모폴로지 연산
kernel = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

# 5. 윤곽선 검출
contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

coin_count = 0

# 동전처럼 보이는 윤곽선만 선택
for cnt in contours:
    area = cv2.contourArea(cnt)

    # 너무 작은 잡음 제거
    if area < 1000:
        continue

    # 초록색 윤곽선 그리기
    cv2.drawContours(result, [cnt], -1, (0, 255, 0), 3)
    coin_count += 1

# 6. 결과 텍스트 출력
cv2.putText(
    result,
    f'Found {coin_count} coins',
    (30, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.2,
    (0, 0, 0),
    3
)

# 결과 출력
cv2.imshow('Gray', gray)
cv2.imshow('Blur', blur)
cv2.imshow('Threshold', thresh)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()