import cv2


src = cv2.imread('\python-opencv\lena.jpg',cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src) # 그레이스케일 영상 전용

cv2.imshow('Source', src)
cv2.imshow('Equalized', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()