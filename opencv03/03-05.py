import cv2

img = cv2.imread('\python-opencv\lena.jpg')
rows, cols, channels = img.shape

#중심좌표, 회전각도, 확대축소비
arr1 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
arr2 = cv2.getRotationMatrix2D(((cols/2)/2, (rows/2)/2),-45,1.2)

dst1 = cv2.warpAffine(img, arr1, (cols, rows))
dst2 = cv2.warpAffine(img, arr2, (cols, rows))

cv2.imshow("",dst1)
cv2.imshow("",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()