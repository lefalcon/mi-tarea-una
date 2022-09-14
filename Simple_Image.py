import cv2
#import numpy as np

img = cv2.imread("../../Pictures/face.png",1)

cv2.imshow("img", img)

print(img.shape)

cv2.waitKey()
