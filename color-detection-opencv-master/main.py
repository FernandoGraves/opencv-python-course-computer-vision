import cv2
from PIL import Image

from util import get_limits #Funcion del creador, en util.py


color_detected = [255, 0, 0]  # color in BGR colorspace
cap = cv2.VideoCapture(0) #Camara 0
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=color_detected)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #Blanco solo lo de color detectado

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox() #Da directamente el x,y de 2 esquinas

    if bbox is not None:
        x1, y1, x2, y2 = bbox #Asigno los x,y obteidos

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) #Dibuji rectangulo en el frame de la camara

    cv2.imshow('frame', frame) #Muestro el frame

    if cv2.waitKey(1) & 0xFF == ord('q'): #Con q me salgo
        break

cap.release()

cv2.destroyAllWindows()

