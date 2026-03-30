#내가 만든 그림판
import cv2
import numpy as np

# 1️⃣ 512x512 흰색 캔버스 생성
canvas = np.ones((512, 512, 3), dtype=np.uint8) * 255

drawing = False  # 드래그 상태
ix, iy = -1, -1  # 시작 좌표

# 2️⃣ 마우스 이벤트 함수
def draw(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y), (0, 0, 0), 3)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


# 창 생성 및 마우스 연결
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', draw)

# 3️⃣ 메인 루프
while True:
    cv2.imshow('Paint', canvas)
    key = cv2.waitKey(1) & 0xFF

    # 4️⃣ c 키 → 초기화
    if key == ord('c'):
        canvas[:] = 255

    # 5️⃣ 종료
    elif key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()