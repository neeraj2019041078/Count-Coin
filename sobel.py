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

    # Apply Sobel operator to calculate gradients
    sobel_x = cv2.Sobel(frame_gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(frame_gray, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate gradient magnitude and direction
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_directi
