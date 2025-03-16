import cv2
import numpy as np

# Load an image
image = cv2.imread('open_cv/image/pikachu.jpeg')  # Replace with your image path

# **Image Arithmetic (Brightness & Contrast)**
bright_image = cv2.add(image, np.array([50.0]))  # Increase brightness
dark_image = cv2.subtract(image, np.array([50.0]))  # Decrease brightness

# **Image Erosion**
kernel = np.ones((5,5), np.uint8)  # Define a 5x5 kernel
eroded_image = cv2.erode(image, kernel, iterations=1)  # Erosion operation

# **Blurring**
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)  # Gaussian Blur

# **Bordering**
bordered_image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 255, 0])  # Green border

# Display images
cv2.imshow("Original", image)
cv2.imshow("Bright Image", bright_image)
cv2.imshow("Dark Image", dark_image)
cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Bordered Image", bordered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
