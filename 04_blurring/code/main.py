import os

import cv2

#El blur se usa para quitar ruido, se hace con una media ponderada entre pixelees


img = cv2.imread(os.path.join('.','data', 'cow-salt-peper.png'))

k_size = 9 #Para vecindad de pixeles usados en el blur
img_blur = cv2.blur(img, (k_size, k_size)) #Usa una vecindad de 7x7
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)
