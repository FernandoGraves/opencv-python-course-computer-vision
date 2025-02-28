import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np
from tensorflow.keras.utils import to_categorical

import cv2

# read webcam
webcam = cv2.VideoCapture(0) #El argumento es el numero de webcam que usamos, si tenemos solo una suele ser 0

# visualize webcam

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): #Si apretamos la q salimos del while
        break

#En la practica los fps de la webcam no se asumen como cada 40ms, lo veremos a detalle despues

webcam.release()
cv2.destroyAllWindows()
