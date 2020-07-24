#To load an image in grayscale

import cv2

img = cv2.imread('test1.png', 1)    #reads image

#Second parameter is -1, 0, 1 for unchanged, b&w, colour respectively

cv2.imshow('in colour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()         #opens window with image, exits on any key press

grey_img = cv2.imread('test1.png',0)

cv2.imshow('in grayscale', grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('test1_grey.png', grey_img)     #creates grey image
