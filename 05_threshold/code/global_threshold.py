import os

import cv2


img = cv2.imread(os.path.join('.','data', 'bear.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Pasamos a escala de grises

ret, thresh_1 = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY) #Si es entre 80 y 255 inclusive, se usa pixel negro, si no es blanco

k_size = 5
thresh_2 = cv2.blur(thresh_1, (k_size, k_size)) #Un blur
ret, thresh_2 = cv2.threshold(thresh_2, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('thresh_1', thresh_1)
cv2.imshow('gray', img_gray)
cv2.imshow('thresh_2', thresh_2)

cv2.waitKey(0)