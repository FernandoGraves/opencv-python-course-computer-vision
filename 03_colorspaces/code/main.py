import os

import cv2


img = cv2.imread(os.path.join('.','data', 'bird_resized.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #A blanco y negro
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Cambia colores, misma info pero de otra forma
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Util en computer vision, para deteccion de colores?

#Aqui se pueden encontrar otras conversiones https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html

print(img_rgb.shape)
print(img_gray.shape)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)
