import os

import cv2


# read video
video_path = os.path.join('.', 'data', 'monkey.mp4')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read() #True si quedan frames, el frame es la imagen

    if ret:
        cv2.imshow('frame', frame) #Muestra el frame
        cv2.waitKey(50) #Muestra el frame por 40ms, asuminendo que el video es de 25 fps

video.release() #Limpia la memoria para el video
cv2.destroyAllWindows() #Cierra las ventanas