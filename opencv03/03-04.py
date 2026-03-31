import cv2

img = cv2.imread('\python-opencv\lena.jpg')
dst1 = cv2.resize(img, (1024,1024), interpolation=cv2.INTER_LINEAR)
dst2 = cv2.resize(img, (1024,1024), interpolation=cv2.INTER_LINEAR)
dst3 = cv2.resize(img, (1024,1024), interpolation=cv2.INTER_LINEAR)


cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
