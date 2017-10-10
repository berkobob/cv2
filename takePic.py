import cv2
import time

cap = cv2.VideoCapture(0)

for i in range(3, 0, -1):
	print (i)
	time.sleep(1)

ret, frame = cap.read()

if ret:
	cv2.imwrite("myPic.jpg", frame)
else:
	print("Failed :(")

cap.release()
cv2.destroyAllWindows()
