import numpy as np
import cv2

cap = cv2.VideoCapture(0)   #(0 is the idx of the camera(we hv only 1 cam hence 0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    edges = cv2.Canny(frame, 100, 200)      #canny
    cv2.imshow('edges video', edges)

    if cv2.waitKey(1) & 0xFF == ord(' '):   #space to exit
        break

cap.release()
cv2.destroyAllWindows()

cap2 = cv2.VideoCapture(0)

while True:
    check,frame = cap2.read()

    c,d  = cv2.pencilSketch(frame, sigma_s=10, sigma_r=0.5, shade_factor=0.015)
    cv2.imshow("Pencil video",c)


    key = cv2.waitKey(1)
    if key == ord(" "):
        break

cap2.release()
cv2.destroyAllWindows()
