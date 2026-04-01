import cv2
img = cv2.imread('\python-opencv\lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 찾고 싶은 부분 (눈) 잘라내기 (템플릿 준비)
template = gray[180:290, 200:360]

# 매칭 수행
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# max_loc이 매칭된 위치의 좌상단 좌표
top_left = max_loc

# 이후 자유롭게 후처리 가능!

print(top_left)
cv2.circle(gray, top_left, 5, (0, 0, 0), -1)

cv2.imshow("gray", gray)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()