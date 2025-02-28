import os

import cv2


img = cv2.imread(os.path.join('.','data', 'whiteboard.png'))

print(img.shape)
cv2.imshow('img_1', img)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3) #Coordenada x, y, thickness 3
cv2.imshow('img_2', img)

# rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1) #Esquinas de los rectangulos, el thickness negativo pinta por dentro
cv2.imshow('img_3', img)

# circle
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10) #Usa el centro y el radio
cv2.imshow('img_4', img)

# text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)
cv2.imshow('img_5', img)

cv2.waitKey(0)
