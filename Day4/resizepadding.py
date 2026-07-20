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

new_height = height // 2
new_width = width // 2

resized = np.zeros((new_height, new_width, channels), dtype=img.dtype)

for i in range(new_height):
    for j in range(new_width):

        old_i = int(i * height / new_height)
        old_j = int(j * width / new_width)

        resized[i][j] = img[old_i][old_j]

cv2.imwrite("resized.jpg", resized)

scale = 1.5

new_height = int(height * scale)
new_width = int(width * scale)

scaled = np.zeros((new_height, new_width, channels), dtype=img.dtype)

for i in range(new_height):
    for j in range(new_width):

        old_i = int(i / scale)
        old_j = int(j / scale)

        if old_i < height and old_j < width:
            scaled[i][j] = img[old_i][old_j]

cv2.imwrite("scaled.jpg", scaled)


rotated = np.zeros((width, height, channels), dtype=img.dtype)

for i in range(height):
    for j in range(width):

        rotated[j][height - 1 - i] = img[i][j]

cv2.imwrite("rotated90.jpg", rotated)


pad = 50

new_height = height + (2 * pad)
new_width = width + (2 * pad)

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