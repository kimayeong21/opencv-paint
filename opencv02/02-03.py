import cv2

src1 = cv2.imread('C:/python-opencv/lena.jpg', cv2.IMREAD_GRAYSCALE)

# 임계점
ret, src2 = cv2.threshold(src1, 160, 255, cv2.THRESH_BINARY)

dst1 = cv2.bitwise_or(src1, src2)
dst2 = cv2.bitwise_not(src1)  # 수정된 부분

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('dst', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()