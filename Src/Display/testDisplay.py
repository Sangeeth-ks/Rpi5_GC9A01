import os
import numpy as np
from PIL import Image
import cv2
# Parameters
width, height = 240, 240  # Image dimensions
xc, yc = 120, 120         # Circle center
radius = 105               # Circle radius
tolerance = 250  # Allowable deviation for the circle boundary
# Create a blank image with a size of 240x240
FRAMEBUFFER = "/dev/fb0"  # Path to the framebuffer device
img_data = np.zeros((240, 240, 3), dtype=np.uint8)  # RGB image with black background
for x in range(width):
    for y in range(height):
        distance_squared = (x - xc)**2 + (y - yc)**2
        if radius**2 - tolerance <= distance_squared <= radius**2 + tolerance:
            img_data[y, x] = [255, 0, 0]  # Set pixel to red


# this is only for testing
# Display the image using OpenCV
cv2.imshow("Circle", img_data)
 
#img_data[50:190, 50:190] = [255, 0,0]  # Draw a red square in the center
r = (img_data[:, :, 0] >> 3).astype(np.uint16)
g = (img_data[:, :, 1] >> 2).astype(np.uint16)
b = (img_data[:, :, 2] >> 3).astype(np.uint16)
img_data = ((r << 11) | (g << 5) | b).astype(np.uint16).tobytes()


# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write to framebuffer
with open(FRAMEBUFFER, "wb") as f:
	f.write(img_data)

