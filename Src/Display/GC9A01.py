import os
import numpy as np
from PIL import Image
import cv2

# Path to your video file
VIDEO_PATH = "/home/sangeeth1994/Downloads/video.mp4"
FRAMEBUFFER = "/dev/fb0"
while True:
	# Open video file
	cap = cv2.VideoCapture(0)

	if not cap.isOpened():
		print("Error: Could not open video file.")
		exit()

	# Get framebuffer resolution using `fbset` command
	fb_width, fb_height = 240, 240  # Update this according to `fbset` output
	fb_bpp = 16  # Bits per pixel (Usually 16 or 32)

	while True:
		ret, frame = cap.read()
		if not ret:
			break  # Exit when video ends

		# Resize frame to match framebuffer resolution
		frame = cv2.resize(frame, (fb_width, fb_height))

		# Convert to RGB565 if using 16-bit framebuffer
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		img = Image.fromarray(frame)

		# Convert image to raw RGB565 format if needed
		if fb_bpp == 16:
			img = img.convert("RGB")
			r, g, b = img.split()
			r = np.array(r) >> 3
			g = np.array(g) >> 2
			b = np.array(b) >> 3
			img_data = (r << 11 | g << 5 | b).astype(np.uint16).tobytes()
		else:
			img_data = img.tobytes()  # 32-bit frame

		# Write to framebuffer
		with open(FRAMEBUFFER, "wb") as f:
			f.write(img_data)

	# Cleanup
	cap.release()
