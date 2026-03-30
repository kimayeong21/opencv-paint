import cv2
import sys

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽 클릭:", x, y)

    elif event == cv2.EVENT_RBUTTONDOWN:
        print("오른쪽 클릭:", x, y)

img = cv2.imread('C:/python-opencv/lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

window_name = 'Lena'

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_callback)

cv2.imshow(window_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()