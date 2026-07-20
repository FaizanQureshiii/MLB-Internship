import cv2
import numpy as np

img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg")

if img is None:
    print("Image not found!")
    exit()

height=len(img)
width=len(img[0])
channels=len(img[0][0])

print("Height :", height)
print("Width  :", width)
print("Channels:", channels)

tx = 200
ty = 100

translated = np.zeros(img.shape, dtype=img.dtype)

for i in range(height):
    for j in range(width):

        new_i = i + ty
        new_j = j + tx

        if new_i < height and new_j < width:
            translated[new_i][new_j] = img[i][j]

cv2.imwrite("translated.jpg", translated)


pad = 50

new_height = height + 2 * pad
new_width = width + 2 * pad

padded = np.zeros((new_height, new_width, channels), dtype=img.dtype)

for i in range(height):
    for j in range(width):
        padded[i + pad][j + pad] = img[i][j]

cv2.imwrite("padded.jpg", padded)



normalized = np.zeros(img.shape, dtype=np.float32)

for i in range(height):
    for j in range(width):
        for c in range(channels):
            normalized[i][j][c] = img[i][j][c] / 255.0

print("Minimum:", normalized.min())
print("Maximum:", normalized.max())