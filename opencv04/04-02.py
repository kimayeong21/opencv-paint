import cv2

img = cv2.imread('\python-opencv\lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.Canny(img, 50, 100)
dst2 = cv2.Canny(img, 50, 200)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()