import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('C:/python-opencv/rail.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

# 원본 복사
src = img.copy()

# 1. 그레이스케일
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 블러
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. 엣지
edges = cv2.Canny(blur, 200, 230)

rows, cols = edges.shape

# 4. ROI (아래 절반)
roi = edges[rows // 2:, :]

# 5. 허프 선 검출
lines = cv2.HoughLinesP(
    roi,
    1,
    np.pi / 180,
    50,
    minLineLength=200,
    maxLineGap=100
)

left_lines = []
right_lines = []

# 선 분류
if lines is not None:
    print("검출된 선 개수:", len(lines))

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # ROI 좌표 → 원본 좌표
        y1_full = y1 + rows // 2
        y2_full = y2 + rows // 2

        if x2 - x1 == 0:
            continue

        slope = (y2_full - y1_full) / (x2 - x1)

        # 수평 제거
        if abs(slope) < 0.5:
            continue

        if slope < 0 and x1 < cols // 2:
            left_lines.append((x1, y1_full, x2, y2_full))

        elif slope > 0 and x1 > cols // 2:
            right_lines.append((x1, y1_full, x2, y2_full))


# 대표선 계산
def make_line(lines):
    if len(lines) == 0:
        return None

    x_points = []
    y_points = []

    for x1, y1, x2, y2 in lines:
        x_points.extend([x1, x2])
        y_points.extend([y1, y2])

    m, b = np.polyfit(y_points, x_points, 1)

    y_bottom = rows
    y_top = int(rows * 0.55)

    x_bottom = int(m * y_bottom + b)
    x_top = int(m * y_top + b)

    return (x_bottom, y_bottom, x_top, y_top)


left_rail = make_line(left_lines)
right_rail = make_line(right_lines)

# 철로 선 그리기
if left_rail is not None:
    cv2.line(src, (left_rail[0], left_rail[1]),
             (left_rail[2], left_rail[3]), (0, 0, 255), 3)

if right_rail is not None:
    cv2.line(src, (right_rail[0], right_rail[1]),
             (right_rail[2], right_rail[3]), (0, 0, 255), 3)

# 중앙 좌표
if left_rail is not None and right_rail is not None:
    center_y = int(rows * 0.8)

    left_x = int(
        left_rail[0] + (center_y - left_rail[1]) *
        (left_rail[2] - left_rail[0]) / (left_rail[3] - left_rail[1] + 1e-6)
    )

    right_x = int(
        right_rail[0] + (center_y - right_rail[1]) *
        (right_rail[2] - right_rail[0]) / (right_rail[3] - right_rail[1] + 1e-6)
    )

    center_x = (left_x + right_x) // 2

    cv2.circle(src, (center_x, center_y), 6, (0, 255, 0), -1)
    cv2.putText(src, f'Center: ({center_x},{center_y})',
                (center_x - 100, center_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# 🔥 출력 (여기 핵심)
cv2.imshow('Gray', gray)
cv2.imshow('Blur', blur)
cv2.imshow('Edges', edges)
cv2.imshow('ROI', roi)
cv2.imshow('Result', src)

cv2.waitKey(0)
cv2.destroyAllWindows()