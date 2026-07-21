import cv2
import numpy as np

img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found!")
    exit()

height, width = img.shape

T = 127

binary = np.zeros((height, width), dtype=np.uint8)
binary_inverse = np.zeros((height, width), dtype=np.uint8)
truncate = np.zeros((height, width), dtype=np.uint8)
to_zero = np.zeros((height, width), dtype=np.uint8)
inverse_to_zero = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        pixel = img[i][j]

        if pixel > T:
            binary[i][j] = 255
        else:
            binary[i][j] = 0

        if pixel > T:
            binary_inverse[i][j] = 0
        else:
            binary_inverse[i][j] = 255

        if pixel > T:
            truncate[i][j] = T
        else:
            truncate[i][j] = pixel

        if pixel > T:
            to_zero[i][j] = pixel
        else:
            to_zero[i][j] = 0

        if pixel > T:
            inverse_to_zero[i][j] = 0
        else:
            inverse_to_zero[i][j] = pixel

cv2.imwrite("binary_threshold.jpg", binary)
cv2.imwrite("binary_inverse_threshold.jpg", binary_inverse)
cv2.imwrite("truncate_threshold.jpg", truncate)
cv2.imwrite("to_zero_threshold.jpg", to_zero)
cv2.imwrite("inverse_to_zero_threshold.jpg", inverse_to_zero)

print("All thresholding operations completed successfully.")