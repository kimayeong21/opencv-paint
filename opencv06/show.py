import cv2
import numpy as np

# 얼굴 검출기
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 호랑이 마스크 PNG (투명 배경)
sticker = cv2.imread('C:/python-opencv/tigermask.png', cv2.IMREAD_UNCHANGED)

if sticker is None:
    print("스티커 이미지 없음")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라 안됨")
    exit()


def overlay_png(background, overlay, x, y, w, h):
    overlay_resized = cv2.resize(overlay, (w, h))

    # 화면 밖으로 나가면 잘라서 처리
    bh, bw = background.shape[:2]

    if x >= bw or y >= bh or x + w <= 0 or y + h <= 0:
        return background

    x1 = max(x, 0)
    y1 = max(y, 0)
    x2 = min(x + w, bw)
    y2 = min(y + h, bh)

    overlay_x1 = x1 - x
    overlay_y1 = y1 - y
    overlay_x2 = overlay_x1 + (x2 - x1)
    overlay_y2 = overlay_y1 + (y2 - y1)

    overlay_crop = overlay_resized[overlay_y1:overlay_y2, overlay_x1:overlay_x2]

    if overlay_crop.shape[2] < 4:
        return background

    alpha = overlay_crop[:, :, 3] / 255.0
    rgb = overlay_crop[:, :, :3]

    for c in range(3):
        background[y1:y2, x1:x2, c] = (
            alpha * rgb[:, :, c] +
            (1 - alpha) * background[y1:y2, x1:x2, c]
        )

    return background


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:
        # 🔥 얼굴 전체보다 크게 덮도록 설정
        sticker_w = int(w * 2.0)
        sticker_h = int(h * 2.0)
        sticker_y = y - int(h * 0.5)

        # 🔥 얼굴 중앙 기준 정렬 + 위로 조금 올리기
        sticker_x = x - int((sticker_w - w) / 2)
        sticker_y = y - int(h * 0.4)

        frame = overlay_png(
            frame,
            sticker,
            sticker_x,
            sticker_y,
            sticker_w,
            sticker_h
        )

    cv2.imshow('SNOW Filter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()