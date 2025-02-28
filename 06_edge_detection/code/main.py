import os

import cv2
import numpy as np


img = cv2.imread(os.path.join('.','data','basketball-player.jpg'))

img_edge = cv2.Canny(img, 100, 200) #Funciona por histeresis, puso el 100 y el 200 por prueba y error

k_size = 3

img_edge_d = cv2.dilate(img_edge, np.ones((k_size, k_size), dtype=np.int8)) #Hace los bords mas gruesos, se usa sobre la imagen ya hecho canny

img_edge_e = cv2.erode(img_edge_d, np.ones((k_size, k_size), dtype=np.int8)) #Hace lo contrario que dilate (En la medida que puede, se pierde informacion en dilate)

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
