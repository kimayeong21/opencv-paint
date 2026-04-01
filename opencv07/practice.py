import cv2
import numpy as np
from collections import deque
import tkinter as tk
from tkinter import colorchooser

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

points = deque(maxlen=1024)

# 기본 색상
draw_color = (0, 0, 255)

# 기본 선 굵기
thickness = 5
min_thickness = 1
max_thickness = 20

# 하늘색 펜 HSV 범위
lower_color = np.array([85, 50, 50])
upper_color = np.array([110, 255, 255])

canvas = None

# tkinter 숨김
root = tk.Tk()
root.withdraw()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.medianBlur(mask, 5)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)

        if cv2.contourArea(cnt) > 500:
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            M = cv2.moments(cnt)

            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

                points.appendleft(center)
    else:
        # 물체가 안 보이면 선이 이상하게 이어지지 않도록 끊기
        points.appendleft(None)

    # 선 그리기
    for i in range(1, len(points)):
        if points[i - 1] is None or points[i] is None:
            continue

        cv2.line(canvas, points[i - 1], points[i], draw_color, thickness)

    result = cv2.add(frame, canvas)

    # 현재 색상 표시
    cv2.rectangle(result, (10, 10), (60, 60), draw_color, -1)

    # 현재 굵기 표시
    cv2.putText(result, f"Thickness: {thickness}", (80, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(result, "C: Clear  P: Color  A: Thick+  S: Thick-  Q: Quit", (80, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

    cv2.imshow("mask", mask)
    cv2.imshow("Air Canvas", result)

    key = cv2.waitKey(1) & 0xFF

    # C → 지우기
    if key == ord('c'):
        canvas = np.zeros_like(frame)
        points.clear()

    # P → 색상 선택
    elif key == ord('p'):
        color = colorchooser.askcolor(title="색 선택")
        if color[0] is not None:
            r, g, b = map(int, color[0])
            draw_color = (b, g, r)
            points.clear()  # 색 바뀐 뒤 새 선부터 적용

    # A → 굵게
    elif key == ord('a'):
        thickness = min(thickness + 2, max_thickness)
        points.clear()  # 굵기 변경 후 새 선부터 적용

    # S → 얇게
    elif key == ord('s'):
        thickness = max(thickness - 2, min_thickness)
        points.clear()  # 굵기 변경 후 새 선부터 적용

    # Q → 종료
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()