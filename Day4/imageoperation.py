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

cv2.imwrite("original.jpg", img)

copy_img = np.zeros(img.shape, dtype=img.dtype)

for i in range(height):
    for j in range(width):
        copy_img[i][j] = img[i][j]

cv2.imwrite("copied.jpg", copy_img)


start_row = 500
end_row = 1500

start_col = 1000
end_col = 2500

crop_height = end_row - start_row
crop_width = end_col - start_col

cropped = np.zeros((crop_height, crop_width, channels), dtype=img.dtype)

for i in range(crop_height):
    for j in range(crop_width):
        cropped[i][j] = img[start_row + i][start_col + j]

cv2.imwrite("cropped.jpg", cropped)

flip_h = np.zeros(img.shape, dtype=img.dtype)

for i in range(height):
    for j in range(width):
        flip_h[i][width - 1 - j] = img[i][j]

cv2.imwrite("flipped_horizontal.jpg", flip_h)

flip_v = np.zeros(img.shape, dtype=img.dtype)

for i in range(height):
    for j in range(width):
        flip_v[height - 1 - i][j] = img[i][j]

cv2.imwrite("flipped_vertical.jpg", flip_v)