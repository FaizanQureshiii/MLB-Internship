import cv2
import numpy as np

# Read grayscale image
img = cv2.imread(r"C:\Users\OTS\Downloads\microsoft-surface-5120x2880-26737.jpg", 0)

# Check if image loaded successfully
if img is None:
    print("Image not found!")
    exit()

# Get image dimensions
height = len(img)
width = len(img[0])

# ---------------- Zero Padding ----------------

# Create a new image with one-pixel border
zero_padding = np.zeros((height + 2, width + 2), dtype=np.uint8)

# Copy original image into the center
for i in range(height):
    for j in range(width):
        zero_padding[i + 1][j + 1] = img[i][j]

# ---------------- Same Padding ----------------

# Create another padded image
same_padding = np.zeros((height + 2, width + 2), dtype=np.uint8)

# Copy original image into the center
for i in range(height):
    for j in range(width):
        same_padding[i + 1][j + 1] = img[i][j]

# Print image sizes
print("Original Image Size :", img.shape)
print("Zero Padding Size   :", zero_padding.shape)
print("Same Padding Size   :", same_padding.shape)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Zero Padding", zero_padding)
cv2.imshow("Same Padding", same_padding)

cv2.waitKey(0)
cv2.destroyAllWindows()