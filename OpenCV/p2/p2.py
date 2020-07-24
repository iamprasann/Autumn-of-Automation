import numpy as np
import cv2

img = cv2.imread('p2.png')      #reading main image
rows,cols = img.shape[:2]

results = []        #all transformations stored in list for easy displaying

#resizing
results.append(cv2.resize(img, None, fx=1.5, fy=0.5, interpolation = cv2.INTER_CUBIC))

#translations
'''Translation is the shifting of object’s location. If you know the shift in (x,y) direction,
let it be (t_x,t_y), you can create the transformation matrix M as follows:
1 0 t_x
0 1 t_y
'''

for i in range(-1, 2):
    M = np.float32([[1,0,-50+(i*50)],[0,1,50-(i*80)]])
    results.append(cv2.warpAffine(img, M, (cols, rows)))

#rotations
'''OpenCV provides a function, cv2.getRotationMatrix2D'''

for i in range(-2, 3):
    M = cv2.getRotationMatrix2D((cols/(abs(i)+1), rows/(abs(i)+1)), -60+45*i, 1)
    results.append(cv2.warpAffine(img, M, (cols, rows)))

#blurs
results.append(cv2.blur(img,(5,5)))
results.append(cv2.GaussianBlur(img,(5,5),0))
results.append(cv2.medianBlur(img,5))

for res in results:
    cv2.imshow('result', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
