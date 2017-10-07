import cv2

img1 = cv2.imread('google.png') 
img2 = cv2.imread('square.png')
img3 = cv2.imread('bird.jpg')

#add = img1 + img2
add = cv2.add(img1, img2)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows, cols,channels = img2.shape
roi = img3[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img3_bg, img2_fg)
img3[0:rows, 0:cols] = dst

cv2.imshow("Merge", img3)
cv2.imshow('Mask', mask)
cv2.imshow('add', add)
cv2.imshow('weighted', weighted)
cv2.imshow('Gray Logo', img2gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
