import cv2
import sys

cap = cv2.VideoCapture(0)
sticker = cv2.imread("C:/python-opencv/tigermask.png", cv2.IMREAD_UNCHANGED)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def overlay_transparent(background, overlay, x, y):
    h, w, _ = background.shape
    ol_h, ol_w, _ = overlay.shape

    if x >= w or y >= h:
        return background

    if x + ol_w > w:
        ol_w = w - x
        overlay = overlay[:, :ol_w]

    if y + ol_h > h:
        ol_h = h - y
        overlay = overlay[:ol_h]

    if x < 0:
        overlay = overlay[:, -x:]
        ol_w = overlay.shape[1]
        x = 0

    if y < 0:
        overlay = overlay[-y:, :]
        ol_h = overlay.shape[0]
        y = 0

    alpha = overlay[:, :, 3] / 255.0
    overlay_img = overlay[:, :, :3]

    for c in range(3):
        background[y:y+ol_h, x:x+ol_w, c] = (
            overlay_img[:, :, c] * alpha +
            background[y:y+ol_h, x:x+ol_w, c] * (1.0 - alpha)
        )

    return background


if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:
            sticker_resized = cv2.resize(
                sticker,
                (int(2.2 * w), int(2.2 * h))
            )

            new_x = x - int(0.6 * w)
            new_y = y - int(0.4 * h)

            frame = overlay_transparent(frame, sticker_resized, new_x, new_y)

        cv2.imshow("frame", frame)

        if cv2.waitKey(20) == 27:
            break
else:
    sys.exit()

cap.release()
cv2.destroyAllWindows()