import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bird.jpg', cv2.IMREAD_GRAYSCALE)

#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

cv2.imshow('Bird', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[250,500], 'c', linewidth=5)
#plt.show()

cv2.imwrite('graybird.png', img)
