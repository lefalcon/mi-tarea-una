# OpenCV no estaa hecho para humanos, es decir, no estaa hecho para ver videos, sino que es para que la compu los analice, por ello se ven rapidiisimo. Si los quieres ver con calma, debes usar FPS como se indica a continuacioon.

import cv2
import time

cap = cv2.VideoCapture("../../Downloads/videotest.mp4")

if not cap.isOpened():
   raise IOError("Cannot open video...")

fps = int(cap.get(cv2.CAP_PROP_FPS))
print('fps = ', fps)

while (True):
#while (cv2.waitKey(10) != 27):
   ret,frame = cap.read()

   if ret == True:
      time.sleep(1/fps)
   
      rz = cv2.resize(frame, (400,300))
      cv2.putText(rz, "Hola mundo...", (30, 200),
                  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
   
      cv2.imshow("Video", rz)

      if cv2.waitKey(1) & 0xFF==ord('q'):
         break
   
   # sii tienes que poner este break, de lo contrario se queda
   # trabado al finalizar el video.
   else: 
      break

cap.release()
cv2.destroyAllWindows()
