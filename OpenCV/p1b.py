import numpy as np
import cv2

cap = cv2.VideoCapture(0)   #(0 is the idx of the camera(we hv only 1 cam hence 0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):   #space to exit
        break

cap.release()
cv2.destroyAllWindows()
