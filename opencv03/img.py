import cv2
import numpy as np

# 이미지 불러오기
orig = cv2.imread('\python-opencv\djkflsa.jpg')
if orig is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

# 화면에 보여줄 크기 축소
scale = 0.5
img = cv2.resize(orig, None, fx=scale, fy=scale)

points = []

def order_points(pts):
    pts = np.array(pts, dtype="float32")

    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    top_left = pts[np.argmin(s)]
    bottom_right = pts[np.argmax(s)]
    top_right = pts[np.argmin(diff)]
    bottom_left = pts[np.argmax(diff)]

    return np.array([top_left, top_right, bottom_right, bottom_left], dtype="float32")

def warp_document():
    global orig, points

    src_pts = order_points(points)

    w1 = np.linalg.norm(src_pts[1] - src_pts[0])
    w2 = np.linalg.norm(src_pts[2] - src_pts[3])
    h1 = np.linalg.norm(src_pts[3] - src_pts[0])
    h2 = np.linalg.norm(src_pts[2] - src_pts[1])

    width = int(max(w1, w2))
    height = int(max(h1, h2))

    dst_pts = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype="float32")

    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
    result = cv2.warpPerspective(orig, matrix, (width, height))

    result_view = cv2.resize(result, None, fx=0.7, fy=0.7)
    cv2.imshow("dst", result_view)

def mouse_callback(event, x, y, flags, param):
    global img, points

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            ox = int(x / scale)
            oy = int(y / scale)

            points.append([ox, oy])
            print(f"{len(points)}번째 점: ({ox}, {oy})")

            cv2.circle(img, (x, y), 6, (255, 0, 0), -1)

            if len(points) > 1:
                prev_x = int(points[-2][0] * scale)
                prev_y = int(points[-2][1] * scale)
                cv2.line(img, (prev_x, prev_y), (x, y), (0, 255, 0), 2)

            if len(points) == 4:
                first_x = int(points[0][0] * scale)
                first_y = int(points[0][1] * scale)
                cv2.line(img, (x, y), (first_x, first_y), (0, 255, 0), 2)

                # 4개 다 찍으면 바로 변환
                warp_document()

cv2.namedWindow("src")
cv2.setMouseCallback("src", mouse_callback)

while True:
    cv2.imshow("src", img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        img = cv2.resize(orig, None, fx=scale, fy=scale)
        points = []
        cv2.destroyWindow("dst")
        print("초기화 완료")

    elif key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()