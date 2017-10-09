import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
