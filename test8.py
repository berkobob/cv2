import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_black = np.array([ 50, 50, 50])
	upper_black = np.array([255,255,255])

	mask = cv2.inRange(hsv, lower_black, upper_black)
	res  = cv2.bitwise_and(frame, frame, mask=mask)

	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)

	#opening removes false positive
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	#closing removes false negatives
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	#tophat = cv2.
	#blackhat = cv2.

	#tophat is diff between input image and opening
	#cv2.imshow('Tophat', tophat)

	#Blackhat is diff between closing and the input image
	#cv2.imshow('blackhat', blackhat)

	cv2.imshow('frame', frame)
	cv2.imshow('res', res)
	cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
