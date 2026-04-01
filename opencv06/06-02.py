import cv2

img = cv2.imread('C:/python-opencv/people.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=7,
    minSize=(60, 60)
)

print("검출된 얼굴 수:", len(faces))

for (x, y, w, h) in faces:
    ratio = w / h
    if ratio < 0.7 or ratio > 1.3:
        continue

    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()