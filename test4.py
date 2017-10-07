import cv2
file1 = "dog.jpeg"
file2 = "bird.jpg"
img = cv2.imread(file2, cv2.IMREAD_COLOR)

px = img[55,55]

print(px)

img[55,55] = [255,255,255]

# Region of Image (ROI)
roi = img[100:150, 100:150]
print(roi)

img[200:300, 150:250] = [255,255,255]

bird = img[40:240, 300:460]
img[0:200, 0:160] = bird

cv2.imshow("Dog", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
