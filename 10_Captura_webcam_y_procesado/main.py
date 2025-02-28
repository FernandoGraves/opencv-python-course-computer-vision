# Reciclando webcam, dibujo en imagen, y recorte de imagen

#Webcam OK
#Dibujo OK
#Escritura OK
#Procesado OK
#Inclusion red neuronal

import cv2

# read webcam
webcam = cv2.VideoCapture(0) #El argumento es el numero de webcam que usamos, si tenemos solo una suele ser 0

#Se definio a partir del print de frame.shape, para el dibujo del rectangulo, centrado y de lado 300x300
dim_x = 640
dim_y = 480
delta_medios = 150
esquina_1 = (int((dim_x)*0.5 - delta_medios),int((dim_y)*0.5 - delta_medios))
esquina_2 = (int((dim_x)*0.5 + delta_medios),int((dim_y)*0.5 + delta_medios))

#Para escritura
origen_texto_instruccion = (10,30)
origen_texto_estado_lechuga = 10,60
estado_lechuga = "FN" #Debe actualizarse desde la inferencia

# visualize webcam

while True:
    ret, frame = webcam.read()

    #Dibujando rectangulo
    #print(frame.shape) #Me dio 640x480 (Se informa como 480x640x3)
    

    # Dibujo del rectangulo
    cv2.rectangle(frame, esquina_1, esquina_2, (0, 255, 0), 2) #Esquinas de los rectangulos, el thickness negativo pinta por dentro

    # Escribo instruccion
    cv2.putText(frame, 'Enfoque la lechuga en el rectangulo!', origen_texto_instruccion, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    # Escribo deteccion
    cv2.putText(frame, 'Estado lechuga: '+ estado_lechuga, origen_texto_estado_lechuga, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    
    #Cortando imagen
    cropped_frame = frame[esquina_1[1]:esquina_2[1],esquina_1[0]:esquina_2[0]] #Corto aprox de 1/3 a 2/3 en ambas dimensiones

    cv2.imshow('frame', frame)
    cv2.imshow('frame_cropped', cropped_frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): #Si apretamos la q salimos del while
        break

#En la practica los fps de la webcam no se asumen como cada 40ms, lo veremos a detalle despues

webcam.release()
cv2.destroyAllWindows()
