# crop
import os

import cv2


img = cv2.imread(os.path.join('.','data', 'bird.jpg'))

print(img.shape) #Es de 168x300

cropped_img = img[32:162,100:200] #Corto aprox de 1/3 a 2/3 en ambas dimensiones

cv2.imshow('img', img) #muestro imagen proginal
cv2.imshow('cropped_img', cropped_img) #Muestro la cortada
cv2.waitKey(2000) 
