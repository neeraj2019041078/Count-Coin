import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny_output = cv2.Canny(frame_gray, 80, 150)

    sobel_x = cv2.Sobel(frame_gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(frame_gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_output = np.sqrt(sobel_x**2 + sobel_y**2)

    laplacian_output = cv2.Laplacian(frame_gray, cv2.CV_64F)

    prewitt_x = cv2.Sobel(frame_gray, cv2.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv2.Sobel(frame_gray, cv2.CV_64F, 0, 1, ksize=3)
    prewitt_output = np.sqrt(prewitt_x**2 + prewitt_y**2)
  

    horrizontal_concat1=cv2.hconcat([frame_gray,canny_output])
    horrizontal_concat2=cv2.hconcat([sobel_output,laplacian_output,prewitt_output])


    final_output=cv2.vconcat([horrizontal_concat1,horrizontal_concat2])

    cv2.imshow('Edge Detection Comparison', final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows() 