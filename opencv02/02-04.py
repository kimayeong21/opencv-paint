import cv2

img = cv2.imread('\python-opencv\lena.jpg')

b, g, r = cv2.split(img)

dst = cv2.merge((r,b,g))

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
cv2.imshow('merge', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()