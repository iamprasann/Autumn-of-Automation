import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX

def give_shape(cnt):
	perimeter=cv2.arcLength(cnt, True)
	approx=cv2.approxPolyDP(cnt, 0.05*perimeter, True)
	area=cv2.contourArea(c)
	if len(approx)==3:
		return 'Triangle'
	if len(approx)==4:
		x,y,w,h=cv2.boundingRect(approx)
		if (w/float(h)>=0.9) and (w/float(h)<=1.1) :
			return 'Square'
		return 'Rectangle'
	(_, _), radius=cv2.minEnclosingCircle(c)
	if abs(area/np.pi*(radius**2))>=0.9 and abs(area/np.pi*(radius**2))<=1.1:
		return 'circle'
	return 'ellipse'

img = cv2.imread("shapes.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("gray", img)
cv2.waitKey(0)

_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
cv2.imshow("black", threshold)
cv2.waitKey(0)

_, contours, k = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	M=cv2.moments(cnt)
	cx=int((M["m10"]/M["m00"]))
	cy=int((M["m01"]/M["m00"]))

	shape=give_shape(cnt)
	final=cv2.putText(img, shape, (cx, cy) , font, 0.3, (0, 0, 0), 2)

cv2.imshow('answer', final)
cv2.waitKey(0)
