import cv2
import numpy as np

# 흰색 배경 생성 (512x512)
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)

# 기존 도형 그리기
cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 5)          # 파란 선
cv2.rectangle(canvas, (50, 200), (200, 400), (0, 255, 0), -1) # 초록 꽉 찬 사각형
cv2.circle(canvas, (350, 300), 100, (0, 0, 255), 3)           # 빨간 원
cv2.putText(canvas, "hello", (180, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# ================= 추가 부분 =================
drawing = False
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y), (0, 0, 0), 3)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw)
# ===========================================


while True:
    cv2.imshow('Canvas', canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break

cv2.destroyAllWindows()