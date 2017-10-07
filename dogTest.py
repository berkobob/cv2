import cv2
img = cv2.imread("dog.jpeg")
cv2.imshow("Dog", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
