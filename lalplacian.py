import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream")
    exit()

plt.figure(figsize=(10, 5))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(frame_gray, cv2.CV_64F)

    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title('Original Frame'), plt.axis('off')

    plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian Edge Detection'), plt.axis('off')

    plt.pause(0.1)
    plt.clf()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
plt.close()
