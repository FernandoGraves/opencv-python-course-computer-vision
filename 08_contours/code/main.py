import os

import cv2


img = cv2.imread(os.path.join('.','data' ,'birds.jpg'))

cv2.imshow('img_original', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) #Queremos los objetos en blanco

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #contoirs son un tipo de lista que continee los bordes de las formas en blanco

min_area_contour = 200

for cnt in contours:
    print(cv2.contourArea(cnt))
    if cv2.contourArea(cnt) > min_area_contour: #Si el area es mayor a 200

        #cv2.drawContours(img, cnt, -1, (0, 0, 255), 1)

        x1, y1, w, h = cv2.boundingRect(cnt) #Rescatamos el rectangulo que bordea el controno del area superior al area minima

        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2) #La dibujamos sobre la imagen original, aunque encontramos los bordes en la que los objetos eran blancos

#print(contours)
cv2.imshow('img', img)
#cv2.imshow('img_gray', img_gray)
#cv2.imshow('thresh', thresh)
cv2.waitKey(0)
