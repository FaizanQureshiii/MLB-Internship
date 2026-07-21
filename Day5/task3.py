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
        histogram[img[i][j]] += 1

cdf = np.zeros(256, dtype=int)

cdf[0] = histogram[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogram[i]

cdf_min = 0

for value in cdf:
    if value != 0:
        cdf_min = value
        break

total_pixels = height * width

normalized_cdf = np.zeros(256, dtype=np.uint8)

for i in range(256):
    normalized_cdf[i] = round(((cdf[i] - cdf_min) / (total_pixels - cdf_min)) * 255)

equalized = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        equalized[i][j] = normalized_cdf[img[i][j]]

cv2.imwrite("equalized_image.jpg", equalized)

equalized_histogram = np.zeros(256, dtype=int)

for i in range(height):
    for j in range(width):
        equalized_histogram[equalized[i][j]] += 1

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.plot(histogram)
plt.title("Original Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.plot(equalized_histogram)
plt.title("Equalized Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()