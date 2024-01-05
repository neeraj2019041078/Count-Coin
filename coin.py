import cv2
import numpy as np


image = cv2.imread('coin.png')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, binary_image = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)


edges = cv2.Canny(binary_image, 30, 150)
cv2.imshow('hello', edges)


contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


coin_count = 0


for contour in contours:
   
    if cv2.contourArea(contour) > 100:
      
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

     
        if len(approx) >= 8:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            coin_count += 1

print(f'Number of coins: {coin_count}')


cv2.imshow('Coins', image)
cv2.waitKey(0)
cv2.destroyAllWindows()