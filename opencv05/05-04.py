import cv2

src = cv2.imread('C:/python-opencv/lena.jpg')
result = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, thresh =  cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierachy = \
cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result = cv2.drawContours(src, contours, -1, (0, 0, 255), 1)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()