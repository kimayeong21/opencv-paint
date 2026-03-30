import cv2
import sys

# 이미지 불러오기
img = cv2.imread('\python-opencv\lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

blue = img[100,100,0]
green = img[100,100,1]
red = img[100,100,2]

print("100행 100열의 색상은? ",blue,green,red)

img[10:100,10:100] = [0,0,0]


cv2.imshow('Lena Window', img)  # 윈도우 창 제목, 이미지 객체

# 키 입력 대기 (아무 키나 누르면 종료)
cv2.waitKey(0)
cv2.destroyAllWindows()