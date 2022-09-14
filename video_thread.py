# OpenCV no estaa hecho para humanos, es decir, no estaa hecho para ver videos, sino que es para que la compu los analice, por ello se ven rapidiisimo. Si los quieres ver con calma, debes usar hilos&/treads, como se indica a continuacioon.

# Se puede mejorar el FPS creado simplemnte un nuevo hilo que lo uunico que hace es obtener de la caamara un nuevo frame, mientras el hilo principal estaa proecesando el frame principal.

# Es decir, usaremos hilos para incrementar el valor fps con OpenCV. Para ello, lo que haremos es mover I/O a otro hilo.Recuerda que I/O es el que lleva a cabo la lectura de frames de la webcam o video.

# Accesar el video usando la funcion cv2.VideoCapture y el meetodo .read() es un "blocking operation". Es decir, el hilo principal de nuestro script de python queda completamente bloqueado ("stalled") hasta que se ha leiido el frame de la camara/video y se regresa a nuestro script.

# Las tareas de I/O son bastante lentas, a comparacioon de "CPU bound operations". De aquii que las aplicaciones con videos lleguen a ser muy pesadas con respecto al CPU (y sobre todo en tiempo real), ya que las tareas I/O son verdaderos cuellos de botella.

# La manera de incrementar el FPS seraa mover la lectura de frames de la webcam o videos a un hilo completamente nuevo y separado totalmente del script principal de python.

# Asi, cuando nuestro programa estee terminado de procesar el frame, el siguiente frame ya estaraa listo para cuando sea llamado.










import cv2
import time
import datetime
from threading import Thread



cap = cv2.VideoCapture("../../Downloads/videotest.mp4")

if not cap.isOpened():
   raise IOError("Cannot open video...")

fps = int(cap.get(cv2.CAP_PROP_FPS))
print('fps = ', fps)


#start = datetime.datetime.now()
start = time.time()
numFrames = 0.

while (True):

   ret,frame = cap.read()




   if ret == True:
      time.sleep(1/fps)

      rz = cv2.resize(frame, (400,300))
      cv2.putText(rz, "Hola mundo...", (250, 200),
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 2)

      
      cv2.imshow("Video", rz)

      if cv2.waitKey(1) & 0xFF==ord('q'):
         break
   
   # sii tienes que poner este break, de lo contrario se queda
   # trabado al finalizar el video.
   else: 
      break

   numFrames += 1

#end = datetime.datetime.now() 
end = time.time()


elapsed = (end-start) #.total_seconds)

#print(datetime.datetime.strptime(str(end), "%Y-%m-%d %H:%M:%S.%f"))
#print(datetime.datetime.strptime(str(elapsed), "%H:%M:%S.%f"))
print("[INFO] elapsed time:", (elapsed))
print("[INFO] approx FPS:", (numFrames/elapsed))

cap.release()
cv2.destroyAllWindows()















