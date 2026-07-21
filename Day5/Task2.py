import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found!")
    exit()

height, width = img.shape

histogram = np.zeros(256, dtype=int)

for i in range(height):
    for j in range(width):
        pixel = img[i][j]
        histogram[pixel] += 1

plt.figure(figsize=(10,5))
plt.plot(histogram)
plt.title("Histogram of Grayscale Image")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")
plt.grid()
plt.show()

dark = np.zeros(img.shape, dtype=np.uint8)
bright = np.zeros(img.shape, dtype=np.uint8)

for i in range(height):
    for j in range(width):

        dark_pixel = img[i][j] - 70
        bright_pixel = img[i][j] + 70

        if dark_pixel < 0:
            dark_pixel = 0

        if bright_pixel > 255:
            bright_pixel = 255

        dark[i][j] = dark_pixel
        bright[i][j] = bright_pixel

cv2.imwrite("dark.jpg", dark)
cv2.imwrite("bright.jpg", bright)

hist_original = np.zeros(256, dtype=int)
hist_dark = np.zeros(256, dtype=int)
hist_bright = np.zeros(256, dtype=int)

for i in range(height):
    for j in range(width):

        hist_original[img[i][j]] += 1
        hist_dark[dark[i][j]] += 1
        hist_bright[bright[i][j]] += 1

        plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(hist_dark)
plt.title("Dark Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixels")

plt.subplot(1,3,2)
plt.plot(hist_original)
plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixels")

plt.subplot(1,3,3)
plt.plot(hist_bright)
plt.title("Bright Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixels")

plt.tight_layout()
plt.show()