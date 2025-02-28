# resizing
import os

import cv2


img = cv2.imread(os.path.join('.','data', 'bird.jpg'))

resized_img = cv2.resize(img, (600,340)) #ancho y alto

print(img.shape) #Printea al reves, alto y ancho
print(resized_img.shape)

cv2.imwrite(os.path.join('.', 'data', 'bird_resized.jpg'), resized_img)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(2000)
