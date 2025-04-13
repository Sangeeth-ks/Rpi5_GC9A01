import os
import numpy as np
from PIL import Image
import cv2
# Create a blank image with a size of 240x240
FRAMEBUFFER = "/dev/fb0"  # Path to the framebuffer device
img_data = np.zeros((240, 240, 3), dtype=np.uint8)  # RGB image with black background

img_data[50:190, 50:190] = [255, 0, 0]  # Draw a red square in the center


# Write to framebuffer
with open(FRAMEBUFFER, "wb") as f:
	f.write(img_data)

