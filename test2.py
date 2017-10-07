import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(2)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('MyVid', frame)
    else:
        print("No video")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
