import cv2

src1 = cv2.imread('\python-opencv\lena.jpg')
src2 = cv2.imread('\python-opencv\lena.jpg')

dst = cv2.addWeighted(src1, 0.3, src2, 0.6, 0)

cv2.imshow('dst', src1)
cv2.waitKey(0)
cv2.destroyAllWindows()