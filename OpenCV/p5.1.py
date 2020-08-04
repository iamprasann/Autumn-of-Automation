import cv2
import numpy as np

cap = cv2.VideoCapture('messi.mp4')
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (3, 3))
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

    if detected_circles is not None:

        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        cv2.imshow("Detected", frame)

cv2.destroyAllWindows()
