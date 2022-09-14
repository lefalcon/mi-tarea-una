import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
   raise IOError("Cannot open webcam...")

while (True):
#while (cv2.waitKey(10) != 27):
   ret,frame = cap.read()
   #print("nada...")
   #if (ret):
   cv2.imshow("WebCam", frame)

   if cv2.waitKey(1) & 0xFF==ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
