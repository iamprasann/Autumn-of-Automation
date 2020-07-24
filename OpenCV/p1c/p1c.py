import cv2

img = cv2.imread('p1c.png', 1)

cv2.imshow('in normal view', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_blue = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

cv2.imshow('red and blue swapped', img_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('p1c_blue.png', img_blue)  
