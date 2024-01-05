import numpy as np
import cv2

img = cv2.imread("coin.png")
image_copy = img.copy()

img = cv2.GaussianBlur(img, (25, 25), 3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 220, 250, cv2.THRESH_BINARY_INV)
cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)
cv2.imshow("thresh", thresh)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

area = {}
temp = 1

for i in range(len(contours)):
    cnt = contours[i]
    ar = cv2.contourArea(cnt)

    if (ar < 930000) and (ar > 1000):
        chosen_cnt = contours[i]
        img_copy = cv2.drawContours(image_copy, [chosen_cnt], -1, (0, 255, 0), 5)

        text = str(temp)
        M = cv2.moments(contours[i])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        cv2.putText(img_copy, text, (cX,cY), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2, cv2.LINE_AA)

        temp += 1

cv2.namedWindow("draw contours", cv2.WINDOW_NORMAL)
cv2.imshow("draw contours", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
