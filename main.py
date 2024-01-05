# import cv2
# import numpy as np


# image = cv2.imread('test1.jpg')
# image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # performing the edge detetcion
# gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
# gradients_sobely = cv2.Sobel(image, -1, 0, 1)
# gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

# gradients_laplacian = cv2.Laplacian(image, -1)

# canny_output = cv2.Canny(image, 80, 150)

# # composite_image = np.concatenate([gradients_sobelx, gradients_sobely, gradients_sobelxy, gradients_laplacian, canny_output], axis=1)

# cv2.imshow('Sobel x', gradients_sobelx)
# cv2.imshow('Sobel y', gradients_sobely)
# cv2.imshow('Sobel X+y', gradients_sobelxy)
# cv2.imshow('laplacian', gradients_laplacian)
# cv2.imshow('Canny', canny_output)
# cv2.waitKey()
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error opening video stream")
    exit()


plt.figure(figsize=(20, 10))

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

   
    plt.clf()

    plt.subplot(2, 3, 1), plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title('Original Frame'), plt.axis('off')

    plt.subplot(2, 3, 2), plt.imshow(canny_output, cmap='gray')
    plt.title('Canny Edge Detection'), plt.axis('off')

    plt.subplot(2, 3, 3), plt.imshow(sobel_output, cmap='gray')
    plt.title('Sobel Edge Detection'), plt.axis('off')

    plt.subplot(2, 3, 4), plt.imshow(laplacian_output, cmap='gray')
    plt.title('Laplacian Edge Detection'), plt.axis('off')

    plt.subplot(2, 3, 5), plt.imshow(prewitt_output, cmap='gray')
    plt.title('Prewitt Edge Detection'), plt.axis('off')

    plt.pause(0.1)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()


plt.close()
