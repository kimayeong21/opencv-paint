import cv2
import numpy as np

def mean_blur(img):
    dst = np.zeros(img.shape, dtype=np.uint8)
    height, width = img.shape

    for y in range(1, height-1):
        for x in range(1, width-1):
            value = img[y - 1, x - 1] + img[y - 1, x] + img[y - 1, x + 1] \
                  + img[y, x - 1] + img[y, x] + img[y, x + 1] \
                  + img[y + 1, x - 1] + img[y + 1, x] + img[y + 1, x + 1]

            value = value / 9

            if value > 255:
                dst[y, x] = 255
            elif value < 0:
                dst[y, x] = 0
            else:
                dst[y, x] = value

    return dst


# =========================
# 이미지 불러오기
# =========================
img = cv2.imread('\python-opencv\lena.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

# =========================
# 직접 구현 평균 블러
# =========================
my_blur = mean_blur(img)

# =========================
# OpenCV 블러 추가 (핵심🔥)
# =========================

# 평균 블러
blur1 = cv2.blur(img, (5, 5))

# 가우시안 블러
blur2 = cv2.GaussianBlur(img, (5, 5), 0)

# 미디언 블러
blur3 = cv2.medianBlur(img, 5)

# =========================
# 결과 출력
# =========================
cv2.imshow('original', img)
cv2.imshow('my_mean_blur', my_blur)
cv2.imshow('cv2.blur', blur1)
cv2.imshow('GaussianBlur', blur2)
cv2.imshow('medianBlur', blur3)

cv2.waitKey(0)
cv2.destroyAllWindows()