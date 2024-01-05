import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open a video capture object (0 for default camera, or provide video file path)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening video stream")
    exit()

# Create a Matplotlib figure for displaying the images
plt.figure(figsize=(15, 5))

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error reading frame")
        break

    # Convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Prewitt operator to calculate gradients
    prewitt_x = cv2.Sobel(frame_gray, cv2.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv2.Sobel(frame_gray, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the gradients to get the Prewitt edge detection result
    prewitt_output = np.sqrt(prewitt_x**2 + prewitt_y**2)

    # Display the original frame and Prewitt edge detection result
    plt.clf()

    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title('Original Frame'), plt.axis('off')

    plt.subplot(1, 2, 2), plt.imshow(prewitt_output, cmap='gray')
    plt.title('Prewitt Edge Detection'), plt.axis('off')

    plt.pause(0.1)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close the Matplotlib figure
plt.close()
